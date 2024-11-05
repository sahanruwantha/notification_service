from django_socio_grpc import generics
import grpc
import logging
from asgiref.sync import sync_to_async
from django.db import transaction
from django_socio_grpc.decorators import grpc_action

from app.models import Notification
from app.serializers import (
    NotificationProtoSerializer,
    SendNotificationRequestSerializer,
    GetUnreadNotificationsRequestSerializer,
    MarkNotificationsAsReadRequestSerializer,
    NotificationListResponseSerializer
)
from app.utils.tasks import dispatch_notifications, get_unread_notifications_utils, mark_notifications_as_read_utils

logger = logging.getLogger(__name__)

class NotificationService(generics.ModelService):
    queryset = Notification.objects.all()
    serializer_class = NotificationProtoSerializer

    @sync_to_async
    def _create_notification(self, request_data):
        """Create a notification in a sync context"""
        with transaction.atomic():
            notification = Notification.objects.create(
                user_id=request_data.user_id,
                type=request_data.type,
                payload=request_data.payload,
                is_read=False
            )
            return notification

    @sync_to_async
    def _serialize_notification(self, notification):
        """Serialize notification in a sync context"""
        serializer = self.get_serializer(notification)
        return serializer.message

    @sync_to_async
    def _get_unread_notifications(self, user_id):
        """Retrieve unread notifications for a specific user in a sync context."""
        notifications = get_unread_notifications_utils(user_id)
        notification_list = [
            {
                'id': n[0],
                'user_id': n[1],
                'payload': n[2],
                'type': n[3],
                'is_read': False
            }
            for n in notifications
        ]
        return notification_list, len(notifications)

    @sync_to_async
    def _serialize_notification_list(self, notifications, count):
        """Serialize notification list in a sync context"""
        serialized_notifications = []
        for notification_dict in notifications:
            serializer = NotificationProtoSerializer(data=notification_dict)
            if serializer.is_valid(raise_exception=True):
                serialized_data = serializer.validated_data
                serialized_data['id'] = notification_dict['id']
                serialized_notifications.append(serialized_data)
        
        response_data = {
            'notifications': serialized_notifications,
            'total_count': count
        }
        print(serialized_notifications)
        response_serializer = NotificationListResponseSerializer(data=response_data)
        if response_serializer.is_valid(raise_exception=True):
            return response_serializer.message
        return None

    @sync_to_async
    def _mark_notifications_as_read(self, notification_ids):
        """Mark notifications as read for a list of notification IDs in a sync context."""
        numbers = ''.join(notification_ids).split(',')
        output_list = [int(num) for num in numbers]
        notification_ids_list = list(output_list)
        return mark_notifications_as_read_utils(notification_ids_list)

    @grpc_action(
        request=SendNotificationRequestSerializer,
        response=NotificationProtoSerializer
    )
    async def Create(self, request, context):
        """Create a notification"""
        try:
            logger.info(f"Processing notification request - Type: {request.type} for User: {request.user_id}")
            
            notification = await self._create_notification(request)
            
            dispatch_notifications(notification.user_id, notification)
            
            return await self._serialize_notification(notification)

        except Exception as e:
            logger.error(f"Failed to send notification: {str(e)}")
            await context.abort(grpc.StatusCode.INTERNAL, f"Failed to send notification: {str(e)}")

    @grpc_action(
        request=GetUnreadNotificationsRequestSerializer,
        response=NotificationListResponseSerializer
    )
    async def GetUnreadNotifications(self, request, context):
        """gRPC method to get unread notifications for a specific user."""
        try:
            notifications, count = await self._get_unread_notifications(request.user_id)
            
            response = await self._serialize_notification_list(notifications, count)
            print('respose', response)
            if response:
                return response
            
            await context.abort(grpc.StatusCode.INTERNAL, "Failed to serialize notifications")

        except Exception as e:
            logger.error(f"Failed to retrieve unread notifications: {str(e)}")
            await context.abort(grpc.StatusCode.INTERNAL, f"Failed to retrieve unread notifications: {str(e)}")

    @grpc_action(request=MarkNotificationsAsReadRequestSerializer)
    async def MarkNotificationsAsRead(self, request, context):
        """gRPC method to mark notifications as read for a list of notification IDs."""
        try:
            updated_count = await self._mark_notifications_as_read(request.user_ids)
            logger.info(f"Marked {updated_count} notifications as read for IDs: {request.user_ids}")
            print(updated_count)
            return updated_count

        except Exception as e:
            logger.error(f"Failed to mark notifications as read: {str(e)}")
            await context.abort(grpc.StatusCode.INTERNAL, f"Failed to mark notifications as read: {str(e)}")
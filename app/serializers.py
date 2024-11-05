from django_socio_grpc import proto_serializers
from rest_framework import serializers
from app.models import Notification
from app.grpc import app_pb2

class NotificationType:
   UNKNOWN = 0
   EMAIL = 1
   ON_SITE = 2
   PUSH = 3

   CHOICES = [
       (UNKNOWN, 'UNKNOWN'),
       (EMAIL, 'EMAIL'),
       (ON_SITE, 'ON_SITE'),
       (PUSH, 'PUSH'),
   ]

class NotificationProtoSerializer(proto_serializers.ModelProtoSerializer):
   id = serializers.IntegerField()
   user_id = serializers.CharField(max_length=200)
   type = serializers.IntegerField()
   payload = serializers.CharField(max_length=200)
   is_read = serializers.BooleanField(default=False)

   def validate_type(self, value):
       if value not in [choice[0] for choice in NotificationType.CHOICES]:
           raise serializers.ValidationError(f"Invalid notification type: {value}")
       return value

   class Meta:
       model = Notification
       proto_class = app_pb2.NotificationRequest 
       proto_class_path = "app_pb2.NotificationRequest" 
       fields = ['id', 'user_id', 'type', 'payload', 'is_read']

class SendNotificationRequestSerializer(proto_serializers.ProtoSerializer):
   id = serializers.IntegerField(read_only=True)
   user_id = serializers.CharField(max_length=200)
   type = serializers.IntegerField(min_value=0, max_value=3) 
   payload = serializers.CharField(max_length=200)
   is_read = serializers.BooleanField(default=False)

   class Meta:
       model = Notification
       proto_class = app_pb2.NotificationResponse 
       proto_class_path = "app_pb2.NotificationResponse" 
       fields = ['user_id', 'type', 'payload']

   def validate_type(self, value):
       if value not in [choice[0] for choice in NotificationType.CHOICES]:
           raise serializers.ValidationError(f"Invalid notification type: {value}")
       return value

   def validate_user_id(self, value):
       if not value:
           raise serializers.ValidationError("User ID cannot be empty")
       return value

   def validate_payload(self, value):
       if not value:
           raise serializers.ValidationError("Payload cannot be empty")
       return value

class NotificationListResponseSerializer(proto_serializers.ProtoSerializer):
   notifications = NotificationProtoSerializer(many=True)
   total_count = serializers.IntegerField()
   
   class Meta:
    proto_class = app_pb2.NotificationListResponse
    proto_class_path = "app_pb2.NotificationListResponse"
    fields = ['notifications', 'total_count']

class NotificationTypeRequestSerializer(proto_serializers.ProtoSerializer):
   type = serializers.IntegerField()

   def validate_type(self, value):
       if value not in [choice[0] for choice in NotificationType.CHOICES]:
           raise serializers.ValidationError(f"Invalid notification type: {value}")
       return value

class NotificationUserRequestSerializer(proto_serializers.ProtoSerializer):
   user_id = serializers.CharField(max_length=200)

   def validate_user_id(self, value):
       if not value:
           raise serializers.ValidationError("User ID cannot be empty")
       return value

class NotificationDeleteRequestSerializer(proto_serializers.ProtoSerializer):
   id = serializers.IntegerField()

   def validate_id(self, value):
       if value < 1:
           raise serializers.ValidationError("Invalid notification ID")
       return value
   
class GetUnreadNotificationsRequestSerializer(proto_serializers.ProtoSerializer):
    user_id = serializers.CharField(max_length=200)

    def validate_user_id(self, value):
        if not value:
            raise serializers.ValidationError("User ID cannot be empty")
        return value

class MarkNotificationsAsReadRequestSerializer(proto_serializers.ProtoSerializer):
    user_ids = serializers.ListField(
        child=serializers.CharField(max_length=200)
    )

    def validate_user_ids(self, value):
        if not value:
            raise serializers.ValidationError("User IDs list cannot be empty")
        return value
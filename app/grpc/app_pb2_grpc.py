# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from app.grpc import app_pb2 as app_dot_grpc_dot_app__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

GRPC_GENERATED_VERSION = '1.67.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in app/grpc/app_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class NotificationControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/notification_service.app.NotificationController/Create',
                request_serializer=app_dot_grpc_dot_app__pb2.SendNotificationRequest.SerializeToString,
                response_deserializer=app_dot_grpc_dot_app__pb2.NotificationResponse.FromString,
                _registered_method=True)
        self.Destroy = channel.unary_unary(
                '/notification_service.app.NotificationController/Destroy',
                request_serializer=app_dot_grpc_dot_app__pb2.NotificationDestroyRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.GetUnreadNotifications = channel.unary_unary(
                '/notification_service.app.NotificationController/GetUnreadNotifications',
                request_serializer=app_dot_grpc_dot_app__pb2.GetUnreadNotificationsRequest.SerializeToString,
                response_deserializer=app_dot_grpc_dot_app__pb2.NotificationListResponse.FromString,
                _registered_method=True)
        self.List = channel.unary_unary(
                '/notification_service.app.NotificationController/List',
                request_serializer=app_dot_grpc_dot_app__pb2.NotificationListRequest.SerializeToString,
                response_deserializer=app_dot_grpc_dot_app__pb2.NotificationListResponse.FromString,
                _registered_method=True)
        self.MarkNotificationsAsRead = channel.unary_unary(
                '/notification_service.app.NotificationController/MarkNotificationsAsRead',
                request_serializer=app_dot_grpc_dot_app__pb2.MarkNotificationsAsReadRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.PartialUpdate = channel.unary_unary(
                '/notification_service.app.NotificationController/PartialUpdate',
                request_serializer=app_dot_grpc_dot_app__pb2.NotificationPartialUpdateRequest.SerializeToString,
                response_deserializer=app_dot_grpc_dot_app__pb2.NotificationResponse.FromString,
                _registered_method=True)
        self.Retrieve = channel.unary_unary(
                '/notification_service.app.NotificationController/Retrieve',
                request_serializer=app_dot_grpc_dot_app__pb2.NotificationRetrieveRequest.SerializeToString,
                response_deserializer=app_dot_grpc_dot_app__pb2.NotificationResponse.FromString,
                _registered_method=True)
        self.Update = channel.unary_unary(
                '/notification_service.app.NotificationController/Update',
                request_serializer=app_dot_grpc_dot_app__pb2.NotificationRequest.SerializeToString,
                response_deserializer=app_dot_grpc_dot_app__pb2.NotificationResponse.FromString,
                _registered_method=True)


class NotificationControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Destroy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUnreadNotifications(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MarkNotificationsAsRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PartialUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Retrieve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NotificationControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=app_dot_grpc_dot_app__pb2.SendNotificationRequest.FromString,
                    response_serializer=app_dot_grpc_dot_app__pb2.NotificationResponse.SerializeToString,
            ),
            'Destroy': grpc.unary_unary_rpc_method_handler(
                    servicer.Destroy,
                    request_deserializer=app_dot_grpc_dot_app__pb2.NotificationDestroyRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetUnreadNotifications': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUnreadNotifications,
                    request_deserializer=app_dot_grpc_dot_app__pb2.GetUnreadNotificationsRequest.FromString,
                    response_serializer=app_dot_grpc_dot_app__pb2.NotificationListResponse.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=app_dot_grpc_dot_app__pb2.NotificationListRequest.FromString,
                    response_serializer=app_dot_grpc_dot_app__pb2.NotificationListResponse.SerializeToString,
            ),
            'MarkNotificationsAsRead': grpc.unary_unary_rpc_method_handler(
                    servicer.MarkNotificationsAsRead,
                    request_deserializer=app_dot_grpc_dot_app__pb2.MarkNotificationsAsReadRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'PartialUpdate': grpc.unary_unary_rpc_method_handler(
                    servicer.PartialUpdate,
                    request_deserializer=app_dot_grpc_dot_app__pb2.NotificationPartialUpdateRequest.FromString,
                    response_serializer=app_dot_grpc_dot_app__pb2.NotificationResponse.SerializeToString,
            ),
            'Retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Retrieve,
                    request_deserializer=app_dot_grpc_dot_app__pb2.NotificationRetrieveRequest.FromString,
                    response_serializer=app_dot_grpc_dot_app__pb2.NotificationResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=app_dot_grpc_dot_app__pb2.NotificationRequest.FromString,
                    response_serializer=app_dot_grpc_dot_app__pb2.NotificationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'notification_service.app.NotificationController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('notification_service.app.NotificationController', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class NotificationController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/notification_service.app.NotificationController/Create',
            app_dot_grpc_dot_app__pb2.SendNotificationRequest.SerializeToString,
            app_dot_grpc_dot_app__pb2.NotificationResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Destroy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/notification_service.app.NotificationController/Destroy',
            app_dot_grpc_dot_app__pb2.NotificationDestroyRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetUnreadNotifications(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/notification_service.app.NotificationController/GetUnreadNotifications',
            app_dot_grpc_dot_app__pb2.GetUnreadNotificationsRequest.SerializeToString,
            app_dot_grpc_dot_app__pb2.NotificationListResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/notification_service.app.NotificationController/List',
            app_dot_grpc_dot_app__pb2.NotificationListRequest.SerializeToString,
            app_dot_grpc_dot_app__pb2.NotificationListResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def MarkNotificationsAsRead(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/notification_service.app.NotificationController/MarkNotificationsAsRead',
            app_dot_grpc_dot_app__pb2.MarkNotificationsAsReadRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def PartialUpdate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/notification_service.app.NotificationController/PartialUpdate',
            app_dot_grpc_dot_app__pb2.NotificationPartialUpdateRequest.SerializeToString,
            app_dot_grpc_dot_app__pb2.NotificationResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Retrieve(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/notification_service.app.NotificationController/Retrieve',
            app_dot_grpc_dot_app__pb2.NotificationRetrieveRequest.SerializeToString,
            app_dot_grpc_dot_app__pb2.NotificationResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/notification_service.app.NotificationController/Update',
            app_dot_grpc_dot_app__pb2.NotificationRequest.SerializeToString,
            app_dot_grpc_dot_app__pb2.NotificationResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

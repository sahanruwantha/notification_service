# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: app/grpc/app.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'app/grpc/app.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x61pp/grpc/app.proto\x12\x18notification_service.app\x1a\x1bgoogle/protobuf/empty.proto\"0\n\x1dGetUnreadNotificationsRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"2\n\x1eMarkNotificationsAsReadRequest\x12\x10\n\x08user_ids\x18\x01 \x03(\t\"(\n\x1aNotificationDestroyRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"\x19\n\x17NotificationListRequest\"v\n\x18NotificationListResponse\x12\x45\n\rnotifications\x18\x01 \x03(\x0b\x32..notification_service.app.NotificationResponse\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"\xac\x01\n NotificationPartialUpdateRequest\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\x05\x12\x0f\n\x07payload\x18\x04 \x01(\t\x12\x14\n\x07is_read\x18\x05 \x01(\x08H\x01\x88\x01\x01\x12\x1e\n\x16_partial_update_fields\x18\x06 \x03(\tB\x05\n\x03_idB\n\n\x08_is_read\"\x7f\n\x13NotificationRequest\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\x05\x12\x0f\n\x07payload\x18\x04 \x01(\t\x12\x14\n\x07is_read\x18\x05 \x01(\x08H\x01\x88\x01\x01\x42\x05\n\x03_idB\n\n\x08_is_read\"\x80\x01\n\x14NotificationResponse\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\x05\x12\x0f\n\x07payload\x18\x04 \x01(\t\x12\x14\n\x07is_read\x18\x05 \x01(\x08H\x01\x88\x01\x01\x42\x05\n\x03_idB\n\n\x08_is_read\")\n\x1bNotificationRetrieveRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"\x83\x01\n\x17SendNotificationRequest\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\x05\x12\x0f\n\x07payload\x18\x04 \x01(\t\x12\x14\n\x07is_read\x18\x05 \x01(\x08H\x01\x88\x01\x01\x42\x05\n\x03_idB\n\n\x08_is_read2\xab\x07\n\x16NotificationController\x12m\n\x06\x43reate\x12\x31.notification_service.app.SendNotificationRequest\x1a..notification_service.app.NotificationResponse\"\x00\x12Y\n\x07\x44\x65stroy\x12\x34.notification_service.app.NotificationDestroyRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x87\x01\n\x16GetUnreadNotifications\x12\x37.notification_service.app.GetUnreadNotificationsRequest\x1a\x32.notification_service.app.NotificationListResponse\"\x00\x12o\n\x04List\x12\x31.notification_service.app.NotificationListRequest\x1a\x32.notification_service.app.NotificationListResponse\"\x00\x12m\n\x17MarkNotificationsAsRead\x12\x38.notification_service.app.MarkNotificationsAsReadRequest\x1a\x16.google.protobuf.Empty\"\x00\x12}\n\rPartialUpdate\x12:.notification_service.app.NotificationPartialUpdateRequest\x1a..notification_service.app.NotificationResponse\"\x00\x12s\n\x08Retrieve\x12\x35.notification_service.app.NotificationRetrieveRequest\x1a..notification_service.app.NotificationResponse\"\x00\x12i\n\x06Update\x12-.notification_service.app.NotificationRequest\x1a..notification_service.app.NotificationResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.grpc.app_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GETUNREADNOTIFICATIONSREQUEST']._serialized_start=77
  _globals['_GETUNREADNOTIFICATIONSREQUEST']._serialized_end=125
  _globals['_MARKNOTIFICATIONSASREADREQUEST']._serialized_start=127
  _globals['_MARKNOTIFICATIONSASREADREQUEST']._serialized_end=177
  _globals['_NOTIFICATIONDESTROYREQUEST']._serialized_start=179
  _globals['_NOTIFICATIONDESTROYREQUEST']._serialized_end=219
  _globals['_NOTIFICATIONLISTREQUEST']._serialized_start=221
  _globals['_NOTIFICATIONLISTREQUEST']._serialized_end=246
  _globals['_NOTIFICATIONLISTRESPONSE']._serialized_start=248
  _globals['_NOTIFICATIONLISTRESPONSE']._serialized_end=366
  _globals['_NOTIFICATIONPARTIALUPDATEREQUEST']._serialized_start=369
  _globals['_NOTIFICATIONPARTIALUPDATEREQUEST']._serialized_end=541
  _globals['_NOTIFICATIONREQUEST']._serialized_start=543
  _globals['_NOTIFICATIONREQUEST']._serialized_end=670
  _globals['_NOTIFICATIONRESPONSE']._serialized_start=673
  _globals['_NOTIFICATIONRESPONSE']._serialized_end=801
  _globals['_NOTIFICATIONRETRIEVEREQUEST']._serialized_start=803
  _globals['_NOTIFICATIONRETRIEVEREQUEST']._serialized_end=844
  _globals['_SENDNOTIFICATIONREQUEST']._serialized_start=847
  _globals['_SENDNOTIFICATIONREQUEST']._serialized_end=978
  _globals['_NOTIFICATIONCONTROLLER']._serialized_start=981
  _globals['_NOTIFICATIONCONTROLLER']._serialized_end=1920
# @@protoc_insertion_point(module_scope)

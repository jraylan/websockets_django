# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wstransport.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11wstransport.proto\"\x19\n\nWSResponse\x12\x0b\n\x03\x61\x63k\x18\x01 \x01(\x08\"[\n\tWSMessage\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x13\n\x06params\x18\x03 \x01(\tH\x01\x88\x01\x01\x42\n\n\x08_messageB\t\n\x07_params\"B\n\x14WSSendMessageRequest\x12\r\n\x05group\x18\x01 \x01(\t\x12\x1b\n\x07message\x18\x02 \x01(\x0b\x32\n.WSMessage2E\n\x0eWSGroupManager\x12\x33\n\x0bSendMessage\x12\x15.WSSendMessageRequest\x1a\x0b.WSResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'wstransport_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _WSRESPONSE._serialized_start=21
  _WSRESPONSE._serialized_end=46
  _WSMESSAGE._serialized_start=48
  _WSMESSAGE._serialized_end=139
  _WSSENDMESSAGEREQUEST._serialized_start=141
  _WSSENDMESSAGEREQUEST._serialized_end=207
  _WSGROUPMANAGER._serialized_start=209
  _WSGROUPMANAGER._serialized_end=278
# @@protoc_insertion_point(module_scope)

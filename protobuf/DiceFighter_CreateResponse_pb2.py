# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import DiceFighter_RetInfo_pb2
import DiceFighter_PlayerInfo_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='DiceFighter_CreateResponse.proto',
  package='cn.senss.server.message',
  serialized_pb='\n DiceFighter_CreateResponse.proto\x12\x17\x63n.senss.server.message\x1a\x19\x44iceFighter_RetInfo.proto\x1a\x1c\x44iceFighter_PlayerInfo.proto\"\x84\x01\n\x0e\x43reateResponse\x12\x0e\n\x06result\x18\x01 \x02(\r\x12\x33\n\x06player\x18\x02 \x02(\x0b\x32#.cn.senss.server.message.PlayerInfo\x12-\n\x03ret\x18\x03 \x02(\x0b\x32 .cn.senss.server.message.RetInfo')




_CREATERESPONSE = descriptor.Descriptor(
  name='CreateResponse',
  full_name='cn.senss.server.message.CreateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='cn.senss.server.message.CreateResponse.result', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='player', full_name='cn.senss.server.message.CreateResponse.player', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ret', full_name='cn.senss.server.message.CreateResponse.ret', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=119,
  serialized_end=251,
)

_CREATERESPONSE.fields_by_name['player'].message_type = DiceFighter_PlayerInfo_pb2._PLAYERINFO
_CREATERESPONSE.fields_by_name['ret'].message_type = DiceFighter_RetInfo_pb2._RETINFO
DESCRIPTOR.message_types_by_name['CreateResponse'] = _CREATERESPONSE

class CreateResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CREATERESPONSE
  
  # @@protoc_insertion_point(class_scope:cn.senss.server.message.CreateResponse)

# @@protoc_insertion_point(module_scope)

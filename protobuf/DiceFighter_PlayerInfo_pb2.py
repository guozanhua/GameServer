# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='DiceFighter_PlayerInfo.proto',
  package='cn.senss.server.message',
  serialized_pb='\n\x1c\x44iceFighter_PlayerInfo.proto\x12\x17\x63n.senss.server.message\"8\n\nPlayerInfo\x12\x0b\n\x03uin\x18\x01 \x02(\r\x12\x0f\n\x07role_id\x18\x02 \x02(\r\x12\x0c\n\x04name\x18\x03 \x02(\t')




_PLAYERINFO = descriptor.Descriptor(
  name='PlayerInfo',
  full_name='cn.senss.server.message.PlayerInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='uin', full_name='cn.senss.server.message.PlayerInfo.uin', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='role_id', full_name='cn.senss.server.message.PlayerInfo.role_id', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='name', full_name='cn.senss.server.message.PlayerInfo.name', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=57,
  serialized_end=113,
)

DESCRIPTOR.message_types_by_name['PlayerInfo'] = _PLAYERINFO

class PlayerInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PLAYERINFO
  
  # @@protoc_insertion_point(class_scope:cn.senss.server.message.PlayerInfo)

# @@protoc_insertion_point(module_scope)

# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='DiceFighter_CreateRequest.proto',
  package='cn.senss.server.message',
  serialized_pb='\n\x1f\x44iceFighter_CreateRequest.proto\x12\x17\x63n.senss.server.message\"-\n\rCreateRequest\x12\x0b\n\x03uin\x18\x01 \x02(\r\x12\x0f\n\x07role_id\x18\x02 \x02(\r')




_CREATEREQUEST = descriptor.Descriptor(
  name='CreateRequest',
  full_name='cn.senss.server.message.CreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='uin', full_name='cn.senss.server.message.CreateRequest.uin', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='role_id', full_name='cn.senss.server.message.CreateRequest.role_id', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=60,
  serialized_end=105,
)

DESCRIPTOR.message_types_by_name['CreateRequest'] = _CREATEREQUEST

class CreateRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CREATEREQUEST
  
  # @@protoc_insertion_point(class_scope:cn.senss.server.message.CreateRequest)

# @@protoc_insertion_point(module_scope)
# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2



_SUPERMARKETGOODSINFO = descriptor.Descriptor(
  name='SuperMarketGoodsInfo',
  full_name='TableProto.SuperMarketGoodsInfo',
  filename='supermarketgoodsinfo.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='TableProto.SuperMarketGoodsInfo.id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='resid', full_name='TableProto.SuperMarketGoodsInfo.resid', index=1,
      number=2, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='groupId', full_name='TableProto.SuperMarketGoodsInfo.groupId', index=2,
      number=3, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='type', full_name='TableProto.SuperMarketGoodsInfo.type', index=3,
      number=4, type=5, cpp_type=1, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='price', full_name='TableProto.SuperMarketGoodsInfo.price', index=4,
      number=5, type=2, cpp_type=6, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='atlas', full_name='TableProto.SuperMarketGoodsInfo.atlas', index=5,
      number=6, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='remark', full_name='TableProto.SuperMarketGoodsInfo.remark', index=6,
      number=7, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='count', full_name='TableProto.SuperMarketGoodsInfo.count', index=7,
      number=8, type=5, cpp_type=1, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sound', full_name='TableProto.SuperMarketGoodsInfo.sound', index=8,
      number=9, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_SUPERMARKETGOODSINFO_ARRAY = descriptor.Descriptor(
  name='SuperMarketGoodsInfo_ARRAY',
  full_name='TableProto.SuperMarketGoodsInfo_ARRAY',
  filename='supermarketgoodsinfo.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='items', full_name='TableProto.SuperMarketGoodsInfo_ARRAY.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_SUPERMARKETGOODSINFO_ARRAY.fields_by_name['items'].message_type = _SUPERMARKETGOODSINFO

class SuperMarketGoodsInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SUPERMARKETGOODSINFO

class SuperMarketGoodsInfo_ARRAY(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SUPERMARKETGOODSINFO_ARRAY


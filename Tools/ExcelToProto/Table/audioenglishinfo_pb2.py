# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2



_AUDIOENGLISHINFO = descriptor.Descriptor(
  name='AudioEnglishInfo',
  full_name='TableProto.AudioEnglishInfo',
  filename='audioenglishinfo.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='TableProto.AudioEnglishInfo.id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='name', full_name='TableProto.AudioEnglishInfo.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='play_state', full_name='TableProto.AudioEnglishInfo.play_state', index=2,
      number=3, type=5, cpp_type=1, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='play_mode', full_name='TableProto.AudioEnglishInfo.play_mode', index=3,
      number=4, type=5, cpp_type=1, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='play_path', full_name='TableProto.AudioEnglishInfo.play_path', index=4,
      number=5, type=5, cpp_type=1, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='action_describe', full_name='TableProto.AudioEnglishInfo.action_describe', index=5,
      number=6, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='audio_describe', full_name='TableProto.AudioEnglishInfo.audio_describe', index=6,
      number=7, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='describe', full_name='TableProto.AudioEnglishInfo.describe', index=7,
      number=8, type=9, cpp_type=9, label=1,
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


_AUDIOENGLISHINFO_ARRAY = descriptor.Descriptor(
  name='AudioEnglishInfo_ARRAY',
  full_name='TableProto.AudioEnglishInfo_ARRAY',
  filename='audioenglishinfo.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='items', full_name='TableProto.AudioEnglishInfo_ARRAY.items', index=0,
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


_AUDIOENGLISHINFO_ARRAY.fields_by_name['items'].message_type = _AUDIOENGLISHINFO

class AudioEnglishInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AUDIOENGLISHINFO

class AudioEnglishInfo_ARRAY(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AUDIOENGLISHINFO_ARRAY


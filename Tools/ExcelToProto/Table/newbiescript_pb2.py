# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2



_NEWBIESCRIPT = descriptor.Descriptor(
  name='NewBieScript',
  full_name='TableProto.NewBieScript',
  filename='newbiescript.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='TableProto.NewBieScript.id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='NewbieId', full_name='TableProto.NewBieScript.NewbieId', index=1,
      number=2, type=13, cpp_type=3, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='Type', full_name='TableProto.NewBieScript.Type', index=2,
      number=3, type=13, cpp_type=3, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='PauseGame', full_name='TableProto.NewBieScript.PauseGame', index=3,
      number=4, type=13, cpp_type=3, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='SoundFileName', full_name='TableProto.NewBieScript.SoundFileName', index=4,
      number=5, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ShowTransparency', full_name='TableProto.NewBieScript.ShowTransparency', index=5,
      number=6, type=13, cpp_type=3, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='FlipType', full_name='TableProto.NewBieScript.FlipType', index=6,
      number=7, type=13, cpp_type=3, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='NotShowArrow', full_name='TableProto.NewBieScript.NotShowArrow', index=7,
      number=8, type=13, cpp_type=3, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='OffsetHighLightX', full_name='TableProto.NewBieScript.OffsetHighLightX', index=8,
      number=9, type=5, cpp_type=1, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='OffsetHighLightY', full_name='TableProto.NewBieScript.OffsetHighLightY', index=9,
      number=10, type=5, cpp_type=1, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='SpecialTip', full_name='TableProto.NewBieScript.SpecialTip', index=10,
      number=11, type=9, cpp_type=9, label=1,
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


_NEWBIESCRIPT_ARRAY = descriptor.Descriptor(
  name='NewBieScript_ARRAY',
  full_name='TableProto.NewBieScript_ARRAY',
  filename='newbiescript.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='items', full_name='TableProto.NewBieScript_ARRAY.items', index=0,
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


_NEWBIESCRIPT_ARRAY.fields_by_name['items'].message_type = _NEWBIESCRIPT

class NewBieScript(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NEWBIESCRIPT

class NewBieScript_ARRAY(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NEWBIESCRIPT_ARRAY

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: order_scheduler.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='order_scheduler.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x15order_scheduler.proto\"K\n\x05Order\x12\x13\n\x04task\x18\x01 \x02(\x0b\x32\x05.Task\x12\x1b\n\x08resource\x18\x02 \x02(\x0b\x32\t.Resource\x12\x10\n\x08order_id\x18\x03 \x01(\t\"#\n\x04Task\x12\x1b\n\tsub_tasks\x18\x01 \x03(\x0b\x32\x08.SubTask\"\x16\n\x07SubTask\x12\x0b\n\x03url\x18\x01 \x02(\t\"=\n\x08Resource\x12\x18\n\x10processors_count\x18\x01 \x02(\x05\x12\x17\n\x0ftime_durability\x18\x02 \x02(\x05\"\x84\x01\n\tStatusMsg\x12%\n\x06status\x18\x02 \x02(\x0e\x32\x15.StatusMsg.StatusType\x12\x0e\n\x06result\x18\x03 \x01(\t\x12\x10\n\x08order_id\x18\x04 \x01(\t\".\n\nStatusType\x12\x08\n\x04\x44ONE\x10\x00\x12\n\n\x06UNDONE\x10\x01\x12\n\n\x06\x46\x41ILED\x10\x02')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_STATUSMSG_STATUSTYPE = _descriptor.EnumDescriptor(
  name='StatusType',
  full_name='StatusMsg.StatusType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNDONE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=313,
  serialized_end=359,
)
_sym_db.RegisterEnumDescriptor(_STATUSMSG_STATUSTYPE)


_ORDER = _descriptor.Descriptor(
  name='Order',
  full_name='Order',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task', full_name='Order.task', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resource', full_name='Order.resource', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='order_id', full_name='Order.order_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=100,
)


_TASK = _descriptor.Descriptor(
  name='Task',
  full_name='Task',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sub_tasks', full_name='Task.sub_tasks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=102,
  serialized_end=137,
)


_SUBTASK = _descriptor.Descriptor(
  name='SubTask',
  full_name='SubTask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='SubTask.url', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=161,
)


_RESOURCE = _descriptor.Descriptor(
  name='Resource',
  full_name='Resource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='processors_count', full_name='Resource.processors_count', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_durability', full_name='Resource.time_durability', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=163,
  serialized_end=224,
)


_STATUSMSG = _descriptor.Descriptor(
  name='StatusMsg',
  full_name='StatusMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='StatusMsg.status', index=0,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result', full_name='StatusMsg.result', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='order_id', full_name='StatusMsg.order_id', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STATUSMSG_STATUSTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=227,
  serialized_end=359,
)

_ORDER.fields_by_name['task'].message_type = _TASK
_ORDER.fields_by_name['resource'].message_type = _RESOURCE
_TASK.fields_by_name['sub_tasks'].message_type = _SUBTASK
_STATUSMSG.fields_by_name['status'].enum_type = _STATUSMSG_STATUSTYPE
_STATUSMSG_STATUSTYPE.containing_type = _STATUSMSG
DESCRIPTOR.message_types_by_name['Order'] = _ORDER
DESCRIPTOR.message_types_by_name['Task'] = _TASK
DESCRIPTOR.message_types_by_name['SubTask'] = _SUBTASK
DESCRIPTOR.message_types_by_name['Resource'] = _RESOURCE
DESCRIPTOR.message_types_by_name['StatusMsg'] = _STATUSMSG

Order = _reflection.GeneratedProtocolMessageType('Order', (_message.Message,), dict(
  DESCRIPTOR = _ORDER,
  __module__ = 'messages.order_scheduler_pb2'
  # @@protoc_insertion_point(class_scope:Order)
  ))
_sym_db.RegisterMessage(Order)

Task = _reflection.GeneratedProtocolMessageType('Task', (_message.Message,), dict(
  DESCRIPTOR = _TASK,
  __module__ = 'messages.order_scheduler_pb2'
  # @@protoc_insertion_point(class_scope:Task)
  ))
_sym_db.RegisterMessage(Task)

SubTask = _reflection.GeneratedProtocolMessageType('SubTask', (_message.Message,), dict(
  DESCRIPTOR = _SUBTASK,
  __module__ = 'messages.order_scheduler_pb2'
  # @@protoc_insertion_point(class_scope:SubTask)
  ))
_sym_db.RegisterMessage(SubTask)

Resource = _reflection.GeneratedProtocolMessageType('Resource', (_message.Message,), dict(
  DESCRIPTOR = _RESOURCE,
  __module__ = 'messages.order_scheduler_pb2'
  # @@protoc_insertion_point(class_scope:Resource)
  ))
_sym_db.RegisterMessage(Resource)

StatusMsg = _reflection.GeneratedProtocolMessageType('StatusMsg', (_message.Message,), dict(
  DESCRIPTOR = _STATUSMSG,
  __module__ = 'messages.order_scheduler_pb2'
  # @@protoc_insertion_point(class_scope:StatusMsg)
  ))
_sym_db.RegisterMessage(StatusMsg)


# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chirpstack-api/as_pb/external/api/profiles.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='chirpstack-api/as_pb/external/api/profiles.proto',
  package='api',
  syntax='proto3',
  serialized_options=b'\n!io.chirpstack.api.as.external.apiB\rProfilesProtoP\001Z7github.com/brocaar/chirpstack-api/go/v3/as/external/api',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n0chirpstack-api/as_pb/external/api/profiles.proto\x12\x03\x61pi\x1a\x1egoogle/protobuf/duration.proto\"\x9e\x05\n\x0eServiceProfile\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x15 \x01(\t\x12\'\n\x0forganization_id\x18\x16 \x01(\x03R\x0eorganizationID\x12*\n\x11network_server_id\x18\x17 \x01(\x03R\x0fnetworkServerID\x12\x0f\n\x07ul_rate\x18\x02 \x01(\r\x12\x16\n\x0eul_bucket_size\x18\x03 \x01(\r\x12\'\n\x0eul_rate_policy\x18\x04 \x01(\x0e\x32\x0f.api.RatePolicy\x12\x0f\n\x07\x64l_rate\x18\x05 \x01(\r\x12\x16\n\x0e\x64l_bucket_size\x18\x06 \x01(\r\x12\'\n\x0e\x64l_rate_policy\x18\x07 \x01(\x0e\x32\x0f.api.RatePolicy\x12&\n\x0f\x61\x64\x64_gw_metadata\x18\x08 \x01(\x08R\raddGWMetaData\x12\x1b\n\x13\x64\x65v_status_req_freq\x18\t \x01(\r\x12!\n\x19report_dev_status_battery\x18\n \x01(\x08\x12 \n\x18report_dev_status_margin\x18\x0b \x01(\x08\x12\x0e\n\x06\x64r_min\x18\x0c \x01(\r\x12\x0e\n\x06\x64r_max\x18\r \x01(\r\x12\x14\n\x0c\x63hannel_mask\x18\x0e \x01(\x0c\x12\x12\n\npr_allowed\x18\x0f \x01(\x08\x12\x12\n\nhr_allowed\x18\x10 \x01(\x08\x12\x12\n\nra_allowed\x18\x11 \x01(\x08\x12\x13\n\x0bnwk_geo_loc\x18\x12 \x01(\x08\x12\x1d\n\ntarget_per\x18\x13 \x01(\rR\ttargetPER\x12(\n\x10min_gw_diversity\x18\x14 \x01(\rR\x0eminGWDiversity\x12\x1f\n\x0bgws_private\x18\x18 \x01(\x08R\ngwsPrivate\"\xe0\x07\n\rDeviceProfile\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x15 \x01(\t\x12\'\n\x0forganization_id\x18\x16 \x01(\x03R\x0eorganizationID\x12*\n\x11network_server_id\x18\x17 \x01(\x03R\x0fnetworkServerID\x12\x18\n\x10supports_class_b\x18\x02 \x01(\x08\x12\x17\n\x0f\x63lass_b_timeout\x18\x03 \x01(\r\x12\x18\n\x10ping_slot_period\x18\x04 \x01(\r\x12 \n\x0cping_slot_dr\x18\x05 \x01(\rR\npingSlotDR\x12\x16\n\x0eping_slot_freq\x18\x06 \x01(\r\x12\x18\n\x10supports_class_c\x18\x07 \x01(\x08\x12\x17\n\x0f\x63lass_c_timeout\x18\x08 \x01(\r\x12\x13\n\x0bmac_version\x18\t \x01(\t\x12\x1b\n\x13reg_params_revision\x18\n \x01(\t\x12\x12\n\nrx_delay_1\x18\x0b \x01(\r\x12#\n\x0erx_dr_offset_1\x18\x0c \x01(\rR\x0brxDROffset1\x12\"\n\rrx_datarate_2\x18\r \x01(\rR\x0brxDataRate2\x12\x11\n\trx_freq_2\x18\x0e \x01(\r\x12\x1c\n\x14\x66\x61\x63tory_preset_freqs\x18\x0f \x03(\r\x12\x19\n\x08max_eirp\x18\x10 \x01(\rR\x07maxEIRP\x12\x16\n\x0emax_duty_cycle\x18\x11 \x01(\r\x12\x15\n\rsupports_join\x18\x12 \x01(\x08\x12\x11\n\trf_region\x18\x13 \x01(\t\x12/\n\x14supports_32bit_f_cnt\x18\x14 \x01(\x08R\x11supports32BitFCnt\x12\x15\n\rpayload_codec\x18\x18 \x01(\t\x12\x1e\n\x16payload_encoder_script\x18\x19 \x01(\t\x12\x1e\n\x16payload_decoder_script\x18\x1a \x01(\t\x12*\n\x11geoloc_buffer_ttl\x18\x1b \x01(\rR\x0fgeolocBufferTTL\x12\x1e\n\x16geoloc_min_buffer_size\x18\x1c \x01(\r\x12*\n\x04tags\x18\x1d \x03(\x0b\x32\x1c.api.DeviceProfile.TagsEntry\x12\x32\n\x0fuplink_interval\x18\x1e \x01(\x0b\x32\x19.google.protobuf.Duration\x12(\n\x10\x61\x64r_algorithm_id\x18\x1f \x01(\tR\x0e\x61\x64rAlgorithmID\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01* \n\nRatePolicy\x12\x08\n\x04\x44ROP\x10\x00\x12\x08\n\x04MARK\x10\x01\x42m\n!io.chirpstack.api.as.external.apiB\rProfilesProtoP\x01Z7github.com/brocaar/chirpstack-api/go/v3/as/external/apib\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,])

_RATEPOLICY = _descriptor.EnumDescriptor(
  name='RatePolicy',
  full_name='api.RatePolicy',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DROP', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MARK', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1757,
  serialized_end=1789,
)
_sym_db.RegisterEnumDescriptor(_RATEPOLICY)

RatePolicy = enum_type_wrapper.EnumTypeWrapper(_RATEPOLICY)
DROP = 0
MARK = 1



_SERVICEPROFILE = _descriptor.Descriptor(
  name='ServiceProfile',
  full_name='api.ServiceProfile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='api.ServiceProfile.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='api.ServiceProfile.name', index=1,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='organization_id', full_name='api.ServiceProfile.organization_id', index=2,
      number=22, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='organizationID', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='network_server_id', full_name='api.ServiceProfile.network_server_id', index=3,
      number=23, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='networkServerID', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ul_rate', full_name='api.ServiceProfile.ul_rate', index=4,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ul_bucket_size', full_name='api.ServiceProfile.ul_bucket_size', index=5,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ul_rate_policy', full_name='api.ServiceProfile.ul_rate_policy', index=6,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dl_rate', full_name='api.ServiceProfile.dl_rate', index=7,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dl_bucket_size', full_name='api.ServiceProfile.dl_bucket_size', index=8,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dl_rate_policy', full_name='api.ServiceProfile.dl_rate_policy', index=9,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='add_gw_metadata', full_name='api.ServiceProfile.add_gw_metadata', index=10,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='addGWMetaData', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dev_status_req_freq', full_name='api.ServiceProfile.dev_status_req_freq', index=11,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='report_dev_status_battery', full_name='api.ServiceProfile.report_dev_status_battery', index=12,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='report_dev_status_margin', full_name='api.ServiceProfile.report_dev_status_margin', index=13,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dr_min', full_name='api.ServiceProfile.dr_min', index=14,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dr_max', full_name='api.ServiceProfile.dr_max', index=15,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channel_mask', full_name='api.ServiceProfile.channel_mask', index=16,
      number=14, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pr_allowed', full_name='api.ServiceProfile.pr_allowed', index=17,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hr_allowed', full_name='api.ServiceProfile.hr_allowed', index=18,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ra_allowed', full_name='api.ServiceProfile.ra_allowed', index=19,
      number=17, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nwk_geo_loc', full_name='api.ServiceProfile.nwk_geo_loc', index=20,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_per', full_name='api.ServiceProfile.target_per', index=21,
      number=19, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='targetPER', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='min_gw_diversity', full_name='api.ServiceProfile.min_gw_diversity', index=22,
      number=20, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='minGWDiversity', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gws_private', full_name='api.ServiceProfile.gws_private', index=23,
      number=24, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='gwsPrivate', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=760,
)


_DEVICEPROFILE_TAGSENTRY = _descriptor.Descriptor(
  name='TagsEntry',
  full_name='api.DeviceProfile.TagsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='api.DeviceProfile.TagsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='api.DeviceProfile.TagsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1712,
  serialized_end=1755,
)

_DEVICEPROFILE = _descriptor.Descriptor(
  name='DeviceProfile',
  full_name='api.DeviceProfile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='api.DeviceProfile.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='api.DeviceProfile.name', index=1,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='organization_id', full_name='api.DeviceProfile.organization_id', index=2,
      number=22, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='organizationID', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='network_server_id', full_name='api.DeviceProfile.network_server_id', index=3,
      number=23, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='networkServerID', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='supports_class_b', full_name='api.DeviceProfile.supports_class_b', index=4,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='class_b_timeout', full_name='api.DeviceProfile.class_b_timeout', index=5,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ping_slot_period', full_name='api.DeviceProfile.ping_slot_period', index=6,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ping_slot_dr', full_name='api.DeviceProfile.ping_slot_dr', index=7,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pingSlotDR', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ping_slot_freq', full_name='api.DeviceProfile.ping_slot_freq', index=8,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='supports_class_c', full_name='api.DeviceProfile.supports_class_c', index=9,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='class_c_timeout', full_name='api.DeviceProfile.class_c_timeout', index=10,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mac_version', full_name='api.DeviceProfile.mac_version', index=11,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reg_params_revision', full_name='api.DeviceProfile.reg_params_revision', index=12,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rx_delay_1', full_name='api.DeviceProfile.rx_delay_1', index=13,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rx_dr_offset_1', full_name='api.DeviceProfile.rx_dr_offset_1', index=14,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='rxDROffset1', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rx_datarate_2', full_name='api.DeviceProfile.rx_datarate_2', index=15,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='rxDataRate2', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rx_freq_2', full_name='api.DeviceProfile.rx_freq_2', index=16,
      number=14, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='factory_preset_freqs', full_name='api.DeviceProfile.factory_preset_freqs', index=17,
      number=15, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_eirp', full_name='api.DeviceProfile.max_eirp', index=18,
      number=16, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='maxEIRP', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_duty_cycle', full_name='api.DeviceProfile.max_duty_cycle', index=19,
      number=17, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='supports_join', full_name='api.DeviceProfile.supports_join', index=20,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rf_region', full_name='api.DeviceProfile.rf_region', index=21,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='supports_32bit_f_cnt', full_name='api.DeviceProfile.supports_32bit_f_cnt', index=22,
      number=20, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='supports32BitFCnt', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload_codec', full_name='api.DeviceProfile.payload_codec', index=23,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload_encoder_script', full_name='api.DeviceProfile.payload_encoder_script', index=24,
      number=25, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload_decoder_script', full_name='api.DeviceProfile.payload_decoder_script', index=25,
      number=26, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='geoloc_buffer_ttl', full_name='api.DeviceProfile.geoloc_buffer_ttl', index=26,
      number=27, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='geolocBufferTTL', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='geoloc_min_buffer_size', full_name='api.DeviceProfile.geoloc_min_buffer_size', index=27,
      number=28, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='api.DeviceProfile.tags', index=28,
      number=29, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uplink_interval', full_name='api.DeviceProfile.uplink_interval', index=29,
      number=30, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='adr_algorithm_id', full_name='api.DeviceProfile.adr_algorithm_id', index=30,
      number=31, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='adrAlgorithmID', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DEVICEPROFILE_TAGSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=763,
  serialized_end=1755,
)

_SERVICEPROFILE.fields_by_name['ul_rate_policy'].enum_type = _RATEPOLICY
_SERVICEPROFILE.fields_by_name['dl_rate_policy'].enum_type = _RATEPOLICY
_DEVICEPROFILE_TAGSENTRY.containing_type = _DEVICEPROFILE
_DEVICEPROFILE.fields_by_name['tags'].message_type = _DEVICEPROFILE_TAGSENTRY
_DEVICEPROFILE.fields_by_name['uplink_interval'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
DESCRIPTOR.message_types_by_name['ServiceProfile'] = _SERVICEPROFILE
DESCRIPTOR.message_types_by_name['DeviceProfile'] = _DEVICEPROFILE
DESCRIPTOR.enum_types_by_name['RatePolicy'] = _RATEPOLICY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ServiceProfile = _reflection.GeneratedProtocolMessageType('ServiceProfile', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEPROFILE,
  '__module__' : 'chirpstack_api.as_pb.external.api.profiles_pb2'
  # @@protoc_insertion_point(class_scope:api.ServiceProfile)
  })
_sym_db.RegisterMessage(ServiceProfile)

DeviceProfile = _reflection.GeneratedProtocolMessageType('DeviceProfile', (_message.Message,), {

  'TagsEntry' : _reflection.GeneratedProtocolMessageType('TagsEntry', (_message.Message,), {
    'DESCRIPTOR' : _DEVICEPROFILE_TAGSENTRY,
    '__module__' : 'chirpstack_api.as_pb.external.api.profiles_pb2'
    # @@protoc_insertion_point(class_scope:api.DeviceProfile.TagsEntry)
    })
  ,
  'DESCRIPTOR' : _DEVICEPROFILE,
  '__module__' : 'chirpstack_api.as_pb.external.api.profiles_pb2'
  # @@protoc_insertion_point(class_scope:api.DeviceProfile)
  })
_sym_db.RegisterMessage(DeviceProfile)
_sym_db.RegisterMessage(DeviceProfile.TagsEntry)


DESCRIPTOR._options = None
_DEVICEPROFILE_TAGSENTRY._options = None
# @@protoc_insertion_point(module_scope)

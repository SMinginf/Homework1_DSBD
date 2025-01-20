# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: financial_service.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'financial_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x66inancial_service.proto\x12\x10\x66inancialservice\x1a\x1egoogle/protobuf/wrappers.proto\"\x8d\x01\n\x0bUserRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x0e\n\x06ticker\x18\x02 \x01(\t\x12.\n\tlow_value\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12/\n\nhigh_value\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\"0\n\x0cUserResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x98\x01\n\rFinancialData\x12\x0e\n\x06ticker\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x02 \x01(\t\x12\x0c\n\x04open\x18\x03 \x01(\x01\x12\x0c\n\x04high\x18\x04 \x01(\x01\x12\x0b\n\x03low\x18\x05 \x01(\x01\x12\r\n\x05\x63lose\x18\x06 \x01(\x01\x12\x0e\n\x06volume\x18\x07 \x01(\r\x12\x11\n\tdividends\x18\x08 \x01(\x02\x12\x0e\n\x06splits\x18\t \x01(\x02\"e\n\x12StockValueResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12-\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x1f.financialservice.FinancialData\x12\x0f\n\x07message\x18\x03 \x01(\t\"3\n\x13StockHistoryRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\x32\xb2\x03\n\x10\x46inancialService\x12M\n\x0cRegisterUser\x12\x1d.financialservice.UserRequest\x1a\x1e.financialservice.UserResponse\x12K\n\nUpdateUser\x12\x1d.financialservice.UserRequest\x1a\x1e.financialservice.UserResponse\x12K\n\nDeleteUser\x12\x1d.financialservice.UserRequest\x1a\x1e.financialservice.UserResponse\x12U\n\x0eGetLatestValue\x12\x1d.financialservice.UserRequest\x1a$.financialservice.StockValueResponse\x12^\n\x0fGetAverageValue\x12%.financialservice.StockHistoryRequest\x1a$.financialservice.StockValueResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'financial_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_USERREQUEST']._serialized_start=78
  _globals['_USERREQUEST']._serialized_end=219
  _globals['_USERRESPONSE']._serialized_start=221
  _globals['_USERRESPONSE']._serialized_end=269
  _globals['_FINANCIALDATA']._serialized_start=272
  _globals['_FINANCIALDATA']._serialized_end=424
  _globals['_STOCKVALUERESPONSE']._serialized_start=426
  _globals['_STOCKVALUERESPONSE']._serialized_end=527
  _globals['_STOCKHISTORYREQUEST']._serialized_start=529
  _globals['_STOCKHISTORYREQUEST']._serialized_end=580
  _globals['_FINANCIALSERVICE']._serialized_start=583
  _globals['_FINANCIALSERVICE']._serialized_end=1017
# @@protoc_insertion_point(module_scope)

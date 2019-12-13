# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import ns2.smpccs_pb2 as smpccs__pb2


class SmpSsmControlStub(object):
  """Definition of the gRPC server
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.PingPong = channel.unary_unary(
        '/SmpSsmControl/PingPong',
        request_serializer=smpccs__pb2.Ping.SerializeToString,
        response_deserializer=smpccs__pb2.Pong.FromString,
        )
    self.ControlSsm = channel.unary_stream(
        '/SmpSsmControl/ControlSsm',
        request_serializer=smpccs__pb2.SsmState.SerializeToString,
        response_deserializer=smpccs__pb2.SsmState.FromString,
        )


class SmpSsmControlServicer(object):
  """Definition of the gRPC server
  """

  def PingPong(self, request, context):
    """A simple RPC to test things.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ControlSsm(self, request, context):
    """A server-to-client streaming RPC.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SmpSsmControlServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'PingPong': grpc.unary_unary_rpc_method_handler(
          servicer.PingPong,
          request_deserializer=smpccs__pb2.Ping.FromString,
          response_serializer=smpccs__pb2.Pong.SerializeToString,
      ),
      'ControlSsm': grpc.unary_stream_rpc_method_handler(
          servicer.ControlSsm,
          request_deserializer=smpccs__pb2.SsmState.FromString,
          response_serializer=smpccs__pb2.SsmState.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'SmpSsmControl', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class SmpSsmUpdateStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.UpdateQuarantine = channel.unary_unary(
        '/SmpSsmUpdate/UpdateQuarantine',
        request_serializer=smpccs__pb2.SsmState.SerializeToString,
        response_deserializer=smpccs__pb2.UpdateResult.FromString,
        )


class SmpSsmUpdateServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def UpdateQuarantine(self, request, context):
    """Send a single state update from clinet to server
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SmpSsmUpdateServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'UpdateQuarantine': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateQuarantine,
          request_deserializer=smpccs__pb2.SsmState.FromString,
          response_serializer=smpccs__pb2.UpdateResult.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'SmpSsmUpdate', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

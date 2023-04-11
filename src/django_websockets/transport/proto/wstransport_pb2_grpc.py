# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import wstransport_pb2 as wstransport__pb2


class WSGroupManagerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendMessage = channel.unary_unary(
                '/WSGroupManager/SendMessage',
                request_serializer=wstransport__pb2.WSSendMessageRequest.SerializeToString,
                response_deserializer=wstransport__pb2.WSResponse.FromString,
                )


class WSGroupManagerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WSGroupManagerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.SendMessage,
                    request_deserializer=wstransport__pb2.WSSendMessageRequest.FromString,
                    response_serializer=wstransport__pb2.WSResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'WSGroupManager', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class WSGroupManager(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/WSGroupManager/SendMessage',
            wstransport__pb2.WSSendMessageRequest.SerializeToString,
            wstransport__pb2.WSResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

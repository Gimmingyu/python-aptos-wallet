from gen import message_pb2, aptos_pb2, aptos_pb2_grpc, message_pb2_grpc


class AptosService(aptos_pb2_grpc.AptosServicer):
    def HealthCheck(self, request, context):
        return message_pb2.HealthCheckOutput(ret="hello world")

    def CreateWallet(self, request, context):
        return super().CreateWallet(request, context)

    def GetBalance(self, request, context):
        return super().GetBalance(request, context)

    def Transfer(self, request, context):
        return super().Transfer(request, context)

import grpc

from gen import message_pb2, aptos_pb2, aptos_pb2_grpc, message_pb2_grpc
from aptos import wallet


class AptosService(aptos_pb2_grpc.AptosServicer):
    def __init__(self):
        self.hd_wallet = wallet.HDWallet("MyHDWallet")
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def HealthCheck(self, request: message_pb2.HealthCheckInput, context):
        return message_pb2.HealthCheckOutput(ret="hello " + request.msg)

    def CreateWallet(self, request: message_pb2.CreateWalletInput, context):
        return super().CreateWallet(request, context)

    def GetBalance(self, request: message_pb2.GetBalanceInput, context):
        return super().GetBalance(request, context)

    def Transfer(self, request: message_pb2.TransferInput, context):
        return super().Transfer(request, context)

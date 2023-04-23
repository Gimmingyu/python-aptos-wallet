import grpc

from gen import message_pb2, aptos_pb2, aptos_pb2_grpc, message_pb2_grpc
from aptos import wallet


class AptosService(aptos_pb2_grpc.AptosServicer):
    def __init__(self):
        self.hd_wallet = wallet.HDWallet()
        pass

    def CreateWallet(self, request: message_pb2.CreateWalletInput, context):
        key = self.hd_wallet.generate_derived_wallet(index=request.user_id)
        return message_pb2.CreateWalletOutput(address=key.address().hex())

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def HealthCheck(self, request: message_pb2.HealthCheckInput, context):
        return message_pb2.HealthCheckOutput(ret="hello " + request.msg)

    def GetBalance(self, request: message_pb2.GetBalanceInput, context):
        return message_pb2.GetBalanceOutput(balance=self.hd_wallet.get_balance(request.address))

    def Transfer(self, request: message_pb2.TransferInput, context):
        self.hd_wallet.transfer(request.to, "to_address", request.amount)
        return message_pb2.TransferOutput(success=True)

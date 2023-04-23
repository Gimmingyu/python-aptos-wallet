from __future__ import print_function
import index
import logging
import grpc
from gen import message_pb2, message_pb2_grpc, aptos_pb2_grpc, aptos_pb2


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = aptos_pb2_grpc.AptosStub(channel)
        response = stub.HealthCheck(message_pb2.HealthCheckInput(msg="primrose"))
    print("Client received: ", response)

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = aptos_pb2_grpc.AptosStub(channel)
        response = stub.CreateWallet(message_pb2.CreateWalletInput(user_id=0))
    print("Client received: ", response)


if __name__ == '__main__':
    logging.basicConfig()
    run()

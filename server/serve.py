from concurrent import futures

from gen import aptos_pb2_grpc
from service import AptosService
import grpc


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    aptos_pb2_grpc.add_AptosServicer_to_server(AptosService(), server)

    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()







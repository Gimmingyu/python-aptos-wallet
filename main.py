from concurrent import futures
import logging

import index
from server import serve

if __name__ == '__main__':
    logging.basicConfig()
    serve.serve()







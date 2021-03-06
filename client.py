import pickle
import socket
import sys

import numpy as np

from util import recv_all

# Get host and port
# host = input("Host: ")
# port = int(input("Port: "))
host = "localhost"
port = 52128

# Attempt connection to server
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
except:
    print("Could not make a connection to the server")
    input("Press enter to quit")
    sys.exit(0)


adjacency_matrix = np.array([1, 2, 3])
start_node = 1
input_ = (adjacency_matrix, start_node)
print(pickle.dumps(input_).hex())
sock.sendall(pickle.dumps(input_))
output = pickle.loads(recv_all(sock))
print(output)

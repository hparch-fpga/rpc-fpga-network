#%%
import pickle
import socket
import sys

from util import highlight_path, recv_all

# Get host and port
# host = input("Host: ")
# port = int(input("Port: "))
host = "localhost"
port = 52128

#%%
# Attempt connection to server
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
except:
    print("Could not make a connection to the server")
    sys.exit(0)


#%%
from graph import adjacency_matrix

highlight_path(adjacency_matrix, [])

#%%
start_node = 10
end_node = 17
input_ = (adjacency_matrix, start_node, end_node)
sock.sendall(pickle.dumps(input_))
output = pickle.loads(recv_all(sock))
highlight_path(adjacency_matrix, output)

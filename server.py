import pickle
import socket
import threading

import networkx as nx
import numpy as np

from util import recv_all


# N = 8
# from pynq import Overlay, Xlnk
# overlay = Overlay("/home/xilinx/matmult/overlay/matmult/matmult.bit")
# dma = overlay.axi_dma_0
# mmult_ip = overlay.dijkstra_1
# xlnk = Xlnk()

# in_buf = xlnk.cma_array(shape=(N, N), dtype=np.int8)
# out_buf = xlnk.cma_array(shape=(N,), dtype=np.int8)


def do_computation(adj: np.ndarray, start_node: int, end_node: int):
    G = nx.from_numpy_matrix(adj)
    path = nx.shortest_path(G, source=start_node, target=end_node)
    return np.array(path)


# Variables for holding information about connections
connections = []
total_connections = 0

# Client class, new instance created for each connected client
# Each instance has the socket and address that is associated with items
# Along with an assigned ID and a name chosen by the client


class Client(threading.Thread):
    def __init__(self, socket: socket.socket, address, id, name, signal):
        threading.Thread.__init__(self)
        self.socket = socket
        self.address = address
        self.id = id
        self.name = name
        self.signal = signal

    def __str__(self):
        return str(self.id) + " " + str(self.address)

    # Attempt to get data from client
    # If unable to, assume client has disconnected and remove him from server data
    # If able to and we get data back, print it in the server and send it back to every
    # client aside from the client that has sent it
    # .decode is used to convert the byte data into a printable string
    def run(self):
        data = recv_all(self.socket)

        if not data:
            return

        return_data = do_computation(*pickle.loads(data))
        if return_data is not None:
            self.socket.send(pickle.dumps(return_data))


def main():
    # Get host and port
    # host = input("Host: ")
    # port = int(input("Port: "))
    host = "localhost"
    port = 52129

    # Create new server socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.bind((host, port))
        sock.listen(5)

        while True:
            s, address = sock.accept()
            global total_connections
            client = Client(s, address, total_connections, "Name", True)
            connections.append(client)
            client.start()
            print("New connection at ID " + str(client))
            total_connections += 1
    finally:
        sock.close()


main()

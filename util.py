import socket
from typing import List

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def recv_all(sock: socket.socket):
    output = bytes()
    while True:
        recvd = sock.recv(2048)
        output += recvd
        if len(recvd) < 2048:
            break

    return output


def highlight_path(adjacency_matrix: np.ndarray, path: List[int]):
    G = nx.convert_matrix.from_numpy_matrix(adjacency_matrix)
    pos = nx.spring_layout(G, seed=2)
    nx.draw(G, pos, node_color="k")
    # draw path in red
    nx.draw_networkx_nodes(G, pos, nodelist=path, node_color="r")
    nx.draw_networkx_labels(G, pos, font_color="w")
    nx.draw_networkx_edges(
        G, pos, edgelist=list(zip(path, path[1:])), edge_color="r", width=1
    )
    # nx.draw_networkx_edge_labels(G, pos)
    plt.axis("equal")
    plt.show()

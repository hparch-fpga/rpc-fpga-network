#%%
from util import highlight_path
import networkx as nx
import numpy as np
import random

G = nx.complete_graph(8)
for (u, v) in G.edges():
    G.edges[u, v]["weight"] = random.randint(0, 10)
nx.draw_networkx(G)

#%%
adjacency_matrix = nx.adjacency_matrix(G).todense().astype(np.uint8)
path = nx.shortest_path(G, source=0)
# highlight_path(adjacency_matrix, [4, 7, 3])

# %%
adjacency_matrix = np.array(
    [
        [0, 3, 1, 0, 0, 0, 7, 2],
        [3, 0, 1, 1, 3, 4, 5, 0],
        [1, 1, 0, 5, 5, 0, 0, 0],
        [0, 1, 5, 0, 1, 0, 0, 2],
        [0, 3, 5, 1, 0, 1, 0, 0],
        [0, 4, 0, 0, 1, 0, 1, 0],
        [7, 5, 0, 0, 0, 1, 0, 0],
        [2, 0, 0, 2, 0, 0, 0, 0],
    ],
    dtype=np.int8,
)
G = nx.from_numpy_matrix(adjacency_matrix)
# nx.draw_networkx(G)
highlight_path(adjacency_matrix, [4, 7, 3])

#%%
for source, path in nx.shortest_path(G, source=0, weight="weight").items():
    cost = sum(G.edges[x, y]["weight"] for x, y in zip(path, path[1:]))
    print(source, path, cost)
# %%

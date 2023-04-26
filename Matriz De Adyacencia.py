import networkx as nx
import matplotlib.pyplot as plt

def is_symmetrical(matrix):
    """
    This function takes a matrix as input and returns True if it is symmetrical, False otherwise.
    """
    n = len(matrix) # get the size of the matrix
    for i in range(n):
        for j in range(i+1, n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

def is_binary_matrix(matrix):
    """
    This function takes a matrix as input and returns True if all its elements are either 0 or 1, False otherwise.
    """
    for row in matrix:
        for element in row:
            if element not in [0, 1]:
                return False
    return True

# create the matrix
matrix = [[0, 2, 3, 7, 4, 5],
           [2, 0, 1, 6, 5, 8],
           [3, 1, 0, 4, 8, 3],
           [7, 6, 4, 0, 2, 9],
           [4, 5, 8, 2, 0, 1],
           [5, 8, 3, 9, 1, 0]]

'''
matrix1 = [[0, 1, 1, 1, 0, 0],
           [1, 0, 1, 0, 0, 0],
           [1, 1, 0, 1, 0, 1],
           [1, 0, 1, 0, 1, 0],
           [0, 0, 0, 1, 0, 1],
           [0, 0, 1, 0, 1, 0]]

matrix2 = [[0, 2, 3, 7, 4, 5],
           [2, 0, 1, 6, 5, 8],
           [3, 1, 0, 4, 8, 3],
           [7, 6, 4, 0, 2, 9],
           [4, 5, 8, 2, 0, 1],
           [5, 8, 3, 9, 1, 0]]
           
matrix3 = [[0, 1, 1, 1, 0, 0],
           [1, 0, 1, 0, 0, 0],
           [0, 1, 0, 1, 1, 1],
           [1, 0, 1, 0, 1, 0],
           [0, 0, 0, 1, 0, 1],
           [0, 0, 1, 0, 1, 0]]

matrix4 = [[0, 2, 3, 4, 0, 0],
           [1, 0, 1, 0, 0, 0],
           [0, 1, 0, 1, 1, 1],
           [1, 0, 1, 0, 1, 0],
           [0, 0, 0, 1, 0, 5],
           [0, 0, 1, 0, 5, 0]]
'''





# create the graph
if is_symmetrical(matrix):
    G = nx.Graph() # undirected graph
else:
    G = nx.DiGraph() # directed graph

# add nodes to the graph
n = len(matrix)
for i in range(n):
    G.add_node(i+1)

# add edges to the graph
for i in range(n):
    for j in range(i+1, n):
        if matrix[i][j] != 0:
            if is_binary_matrix(matrix):
                G.add_edge(i+1, j+1)
            else:
                G.add_edge(i+1, j+1, weight=matrix[i][j])

# draw the graph
pos = nx.spring_layout(G) # positions for all nodes
if is_binary_matrix(matrix):
    nx.draw(G, pos, with_labels=True) # draw nodes and edges
else:
    labels = nx.get_edge_attributes(G, "weight") # get edge weights as labels
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels) # draw labels on edges
    nx.draw(G, pos, with_labels=True) # draw nodes and edges
plt.show() # show the plot
import hashlib
from math import sqrt

y_list = [20,93,72,35,54,95,25,37,29,72,65,66,49,43,35,61,97,66,64,22,83,69,19,21,69,40,35,81,15,41,74,12,3,65,
          31,12,48,68,41,40,99,13,70,30,20,35,84,96,1,93,61,83,24,27,93,86,96,43,10,51,27,87,40,35,83,44,15,89,
          71,79,25,84,43,49,66,0,88,80,4,3,74,10,41,45,75,34,41,44,50,99,41,37,26,6,94,94,76,48,32,42]

# string containing all y values
y_values = "209372355495253729726566494335619766642283691921694035811541741236531124868414099137030203584961936183242793" \
           "86964310512787403583441589717925844349660888043741041457534414450994137266949476483242"

# SHA256 hash of y values
sha256_received = "5c14e4599f1d2a39abe6b487ac2a5415c894c6882f5fdd4a40e02c7dd628829a"

def test_data():
    m = hashlib.sha256()
    m.update(y_values.encode('ascii'))
    sha256_generated = m.hexdigest()

    return sha256_received == sha256_generated

print(test_data())

class Point(object):
    """represents a coordinate"""
    def __init__(self, num1, num2):
        self.x = num1
        self.y = num2

    def distance(self, p2):
        dx = self.x - p2.x
        dy = self.y - p2.y
        return sqrt(dx * dx + dy * dy)

    def __str__(self):
        return "x: " + str(self.x) + " y: " + str(self.y)

# Constructor
  # Number of edges
  # Adjacancy matrix, adjacency list, list of edges

# Methods for adding edges

# Methods for removing edges

# Methods for searching a graph
  # BFS, DFS, Dijkstra, A*...

# Methods for finding a minimum spanning tree
  # Prim's algorithm, Kruskal's algorithm, Borůvka's algorithm...

# Other interesting methods

class Graph():
    """ Graph data structure, undirected by default"""
    def __init__(self):
        self.graph = {}
        self.__create_graph()

    def __generate(self):
        """generates 100 Point objects"""
        l = []
        for item, el in zip(range(1, 101), y_list):
            p = Point(item, el)
            l.append(p)
        return l

    def __create_graph(self):
        """finds neighbours for each point/node"""
        l = self.__generate()
        dist = 20
        for el in l:
            neighbours = {}
            for j in l:
                d = el.distance(j)
                if d <= dist and el != j:
                    neighbours[j] = d
            self.graph[el] = neighbours

    def __str__(self):
        s = ""
        for (key, value) in self.graph.items():
            s += f'key: {key} \n'
            # distances = []
            for (key, value) in value.items():
                s += f'{key} distance: {value} \n'
                #distances.append(value)
            # m = min(distances)
            # print(f'minimum: {m}')
        return s

g = Graph()
print(g)


"""
        matrix_elements = sorted(self.graph, key=lambda x: x.x)
        cols = rows = len(matrix_elements)

        adjacency_matrix = [[0 for x in range(rows)] for y in range(cols)]
        edges_list = []

        for key in matrix_elements:
            for (neighbor, distance) in self.graph[key].items():
                edges_list.append((key, neighbor))

        for edge in edges_list:
            index_of_first_vertex = matrix_elements.index(edge[0])
            index_of_second_vertex = matrix_elements.index(edge[1])
            adjacency_matrix[index_of_first_vertex][index_of_second_vertex] = 1 # distance
        print(adjacency_matrix)
"""
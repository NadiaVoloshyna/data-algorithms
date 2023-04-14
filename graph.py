import hashlib
from math import sqrt
from collections import deque

# values for y
y_list = [20,93,72,35,54,95,25,37,29,72,65,66,49,43,35,61,97,66,64,22,83,69,19,21,69,40,35,81,15,41,74,12,3,65,
          31,12,48,68,41,40,99,13,70,30,20,35,84,96,1,93,61,83,24,27,93,86,96,43,10,51,27,87,40,35,83,44,15,89,
          71,79,25,84,43,49,66,0,88,80,4,3,74,10,41,45,75,34,41,44,50,99,41,37,26,6,94,94,76,48,32,42]

# string containing all y values
y_values = "209372355495253729726566494335619766642283691921694035811541741236531124868414099137030203584961936183242793" \
           "86964310512787403583441589717925844349660888043741041457534414450994137266949476483242"

# SHA256 hash of y values
sha256_received = "5c14e4599f1d2a39abe6b487ac2a5415c894c6882f5fdd4a40e02c7dd628829a"

def test_data():
    """checks the validity of test data by calculating a SHA256 checksum"""
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

class Graph():
    """ Graph data structure"""
    def __init__(self, points):
        self.points = points
        self.graph = {}
        self.edges_list = []
        self.add_points()
        self.add_edges()

    def add_points(self):
        for p in self.points:
            self.add_point(p)

    def add_edges(self):
        for p in self.points:
            for (neighbor, distance) in self.graph[p].items():
                self.add_edge(p, neighbor, distance)

    def add_point(self, p):
        """finds neighbours for the point"""
        dist = 20
        neighbours = {}
        for el in self.points:
            d = p.distance(el)
            if d <= dist and el != p:
                neighbours[el] = d
        self.graph[p] = neighbours

    def add_edge(self, p1, p2, d):
        self.edges_list.append((p1, p2, d))

    def search(self):
        root = list(self.graph.keys())[0]
        visited = []
        q = deque([root])
        visited.append((root))
        while len(q) > 0:
            node = q.popleft()
            neighbours = self.graph[node].keys()
            remaining = set(neighbours).difference(set(visited))
            if len(remaining) > 0:
                for el in remaining:
                    visited.append(el)
                    q.append(el)

        return visited

    # def find(self, parent, i):
    #     if parent[i] != i:
    #         parent[i] = self.find(parent, parent[i])
    #     return parent[i]

    def find(self, parent, i):
        if parent[i] == i:
            return i
        else:
            return self.find(parent, parent[i])

    # def union(self, parent, rank, x, y):
    #     if rank[x] < rank[y]:
    #         parent[x] = y
    #     elif rank[x] > rank[y]:
    #         parent[y] = x
    #     else:
    #         parent[y] = x
    #         rank[x] += 1

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # def mst(self):
    #     result = []
    #     i = e = 0
    #     sorted_edges = sorted(self.edges_list, key=lambda x: x[2])
    #     parent = {}
    #     rank = dict.fromkeys(self.points, 0)
    #
    #     for node in self.points:
    #         parent[node] = node
    #
    #     while e < len(self.points) - 1:
    #         u, v, w = sorted_edges[i]
    #         i = i + 1
    #         x = self.find(parent, u)
    #         y = self.find(parent, v)
    #         if x != y:
    #             e = e + 1
    #             result.append([u, v, w])
    #             self.union(parent, rank, x, y)
    #
    #     for s, d, w in result:
    #         print("%s - %s: %s" % (s, d, w))
    #     print(len(result))

    def mst(self):
        result = []
        i, e = 0, 0
        sorted_edges = sorted(self.edges_list, key=lambda x: x[2])
        parent = {}
        rank = dict.fromkeys(self.points, 0)
        for node in self.points:
            parent[node] = node

        while e < len(self.points) - 1:
            s, d, w = sorted_edges[i]
            i += 1
            x = self.find(parent, s)
            y = self.find(parent, d)
            if x != y:
                e += 1
                result.append([s, d, w])
                self.union(parent, rank, x, y)
        for s, d, w in result:
            print("%s - %s: %s" % (s, d, w))
        print(len(result))

    def __str__(self):
        s = ""
        for (key, value) in self.graph.items():
            s += f'key: {key} \n'
            for (key, value) in value.items():
                s += f'{key} distance: {value} \n'
        return s

def generate():
    """generates 100 Point objects"""
    l = []
    for item, el in zip(range(1, 101), y_list):
        p = Point(item, el)
        l.append(p)
    return l

def graph_demo():
    points = generate()
    g = Graph(points)
    g.mst()
    #print(g)

graph_demo()

"""
plt.figure()
nx.draw_networkx(T, pos=pos2, with_labels=False, node_size = 15)
plt.show()
"""
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
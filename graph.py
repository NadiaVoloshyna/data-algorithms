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
        self.graph = {}
        self.edges_list = []
        self.add_points(points)
        self.add_edges(points)

    def add_points(self, points):
        """finds neighbours for each point/node"""
        dist = 20
        for el in points:
            neighbours = {}
            for j in points:
                d = el.distance(j)
                if d <= dist and el != j:
                    neighbours[j] = d
            self.graph[el] = neighbours

    def add_edges(self, points):
        for p in points:
            for (neighbor, distance) in self.graph[p].items():
                self.edges_list.append((p, neighbor, distance))

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

        #sorted_edges = sorted(self.edges_list, key = lambda x: x[2])

    def find_path(self, point, n):
        neighbours = self.graph[point]
        sorted_neighbours = {key: val for key, val in sorted(neighbours.items(), key=lambda el: el[1])}
        if n >= len(list(sorted_neighbours.keys())):
            return None, None
        next_point = list(sorted_neighbours.keys())[n]
        next_point_distance = list(sorted_neighbours.values())[n]

        return next_point, next_point_distance

    def test(self, prev, root, result):
        if root is None or prev is None:
            return result
        prev_next = 0
        d1 = 0
        c = 1
        while True:
            if prev_next not in result and prev_next != 0 or prev_next == None:
                break
            prev_next, d1 = self.find_path(prev,c)
            c += 1
        root_next = 0
        d2 = 0
        n = 1
        while True:
            if root_next not in result and root_next != 0 and root_next != prev_next  or root_next == None:
                break
            root_next, d2 = self.find_path(root,n)
            n += 1
        if d1 > d2 or d1 == None:
            prev = root
            root = root_next
        elif d2 > d1 or d2 == None:
            prev = prev
            root = prev_next

        result.append(root)

        self.test(prev, root, result)

    def mst(self, points):
        root = points[0]
        next, d = self.find_path(root, 0)
        result = [root, next]
        self.test(root, next, result)

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
    g.mst(points)
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
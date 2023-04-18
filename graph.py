import hashlib
from math import sqrt
from collections import deque
import drawsvg as draw

# values for y
y_list = [20,93,72,35,54,95,25,37,29,72,65,66,49,43,35,61,97,66,64,22,83,69,19,21,69,40,35,81,15,41,74,12,3,65,
          31,12,48,68,41,40,99,13,70,30,20,35,84,96,1,93,61,83,24,27,93,86,96,43,10,51,27,87,40,35,83,44,15,89,
          71,79,25,84,43,49,66,0,88,80,4,3,74,10,41,45,75,34,41,44,50,99,41,37,26,6,94,94,76,48,32,42]

# string containing y values
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

print(f'data is valid: {test_data()}')

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
        self.vertices = points
        self.graph = {}
        self.edges_list = []
        self.mst = []
        self.add_vertices()
        self.add_edges()

    def add_vertices(self):
        for p in self.vertices:
            self.add_vertex(p)

    def add_edges(self):
        for p in self.vertices:
            for (neighbor, distance) in self.graph[p].items():
                self.add_edge(p, neighbor, distance)

    def add_vertex(self, p):
        """finds neighbours for the point"""
        dist = 20
        neighbours = {}
        for el in self.vertices:
            d = p.distance(el)
            if d <= dist and el != p:
                neighbours[el] = d
        self.graph[p] = neighbours

    def add_edge(self, p1, p2, d):
        self.edges_list.append((p1, p2, d))

    def search(self):
        """traverses all nodes of the graph"""
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

    def find(self, parent, i):
        """a utility function to find set of an element i"""
        if parent[i] == i:
            return i
        else:
            return self.find(parent, parent[i])

    def union(self, parent, subtree_sizes, x, y):
        """a function that does union of two sets of x and y"""
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)
        if subtree_sizes[x_root] < subtree_sizes[y_root]:
            parent[x_root] = y_root
        elif subtree_sizes[x_root] > subtree_sizes[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            subtree_sizes[x_root] += 1

    def spanning_tree(self):
        """the main function to construct MST"""
        i, e = 0, 0
        sorted_edges = sorted(self.edges_list, key=lambda x: x[2])
        parent = {}
        subtree_sizes = dict.fromkeys(self.vertices, 0)
        for node in self.vertices:
            parent[node] = node

        while e < len(self.vertices) - 1:
            node1, node2, weight = sorted_edges[i]
            i += 1
            x = self.find(parent, node1)
            y = self.find(parent, node2)
            if x != y:
                e += 1
                self.mst.append([node1, node2, weight])
                self.union(parent, subtree_sizes, x, y)

    def mst_svg(self):
        """generates SVG image for MST"""
        d = draw.Drawing(800, 800, id_prefix = 'd', viewBox="-10 -10 130 130")
        for edge in self.mst:
            node1, node2, weight = edge
            weight = round(weight)
            d.append(draw.Line(node1.x, node1.y,
                               node2.x, node2.y,
                               stroke='blue', stroke_width=0.5, fill='none', marker_end=''))
            d.append(draw.Text(str(weight), font_size=2,
                               x=(node1.x + node2.x) / 2, y=(node1.y + node2.y) / 2,
                               stroke_width=0.1, fill='red'))
        for vertex in self.vertices:
            d.append(draw.Circle(vertex.x, vertex.y, 0.7, fill='red', stroke_width=0.7))
        d.save_svg('mst.svg')

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
    g.spanning_tree()
    g.mst_svg()
    print(g)

graph_demo()


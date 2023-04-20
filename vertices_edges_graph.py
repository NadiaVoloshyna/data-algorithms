class Vertex():
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_name(self):
        return self.name

class Edge():
    def __init__(self, left_vertex, right_vertex):
        self.left_vertex = left_vertex
        self.right_vertex = right_vertex

    def get_left_vertex(self):
        return self.left_vertex

    def get_right_vertex(self):
        return self.right_vertex

class Graph():
    def __init__(self):
        self.vertices = []
        self.edges = []

    def add_vertex(self, x, y, name):
        self.vertices.append(Vertex(x, y, name))

    def add_edge(self, left_vertex, right_vertex):
        self.edges.append(Edge(left_vertex, right_vertex))

    def get_vertices(self):
        return self.vertices

    def get_edges(self):
        return self.edges

    def get_vertex_dict(self):
        return

    def __str__(self):
        s = ""
        for (el) in self.vertices:
            s += f'x: {el.x} y: {el.y} name: {el.name} \n'
        for el in self.edges:
            s += f'left_edge: x: {el.left_vertex.x} y: {el.left_vertex.y} name: {el.left_vertex.name}   '
            s += f'right_edge: x: {el.right_vertex.x} y: {el.right_vertex.y} name: {el.right_vertex.name}'
        return s

def demo():
    a = Vertex(1,1,'A')
    b = Vertex(3,3,'B')
    g = Graph()
    g.add_vertex(1,1,'A')
    g.add_vertex(3,3,'B')
    g.add_edge(a,b)
    print(g)

demo()



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
        self.d = {}

    def add_vertex(self, x, y, name):
        self.vertices.append(Vertex(x, y, name))

    def add_edge(self, left_vertex, right_vertex):
        self.edges.append(Edge(left_vertex, right_vertex))

    def get_vertices(self):
        return self.vertices

    def get_edges(self):
        return self.edges

    def vertex_dict(self):
        for el in self.vertices:
            self.d.setdefault(el.get_name(), [])
            for edge in self.edges:
                if el.get_name() == edge.get_left_vertex().get_name():
                    self.d[el.get_name()].append(edge.get_right_vertex().get_name())

    def __str__(self):
        s = ""
        for (el) in self.vertices:
            s += f'x: {el.x} y: {el.y} name: {el.name} \n'
        for el in self.edges:
            s += f'left_edge: x: {el.left_vertex.x} y: {el.left_vertex.y} name: {el.left_vertex.name}   '
            s += f'right_edge: x: {el.right_vertex.x} y: {el.right_vertex.y} name: {el.right_vertex.name} \n'
        for (key, value) in self.d.items():
            s += f'{key}: {value} \n'
        return s

def demo():
    # a = Vertex(1, 1, 'A')
    # b = Vertex(3, 3, 'B')
    # c = Vertex(5, 5, 'C')
    # d = Vertex(7, 7, 'D')
    # g = Graph()
    # g.add_vertex(1, 1, 'A')
    # g.add_vertex(3, 3, 'B')
    # g.add_vertex(5, 5, 'C')
    # g.add_vertex(7, 7, 'D')
    # g.add_edge(a, b)
    # g.add_edge(c, d)
    # g.vertex_dict()
    # print(g)
    g = Graph()
    letter = 65
    for x in range( 100, 500, 100 ):
        g.add_vertex(x, x + 50, chr( letter ) )
        letter += 1

    v_list = g.get_vertices()
    for v1 in v_list:
        for v2 in v_list:
            if v1.get_name() < v2.get_name():
                g.add_edge(v1, v2)
    g.vertex_dict()
    print(g)

demo()



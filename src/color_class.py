class ColorClass:

    def __init__(self, colornum, list_of_vertices=None):
        self.colornum = colornum
        if list_of_vertices is None:
            self.vertices = []
        else:
            self.vertices = list_of_vertices

    def size(self):
        return len(self.vertices)

    def add_vertex(self, vertex):
        self.vertices.append(vertex)

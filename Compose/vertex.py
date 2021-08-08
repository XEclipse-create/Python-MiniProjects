import random

class vertex:
    def __init__(self,value):
        self.value = value
        self.adjacent = {}
        self.neigh = []
        self.weight =[]

    def add_edge(self,v,w=0):
        self.adjacent[v] = w
    
    def increment(self, v):
        self.adjacent[v] = self.adjacent.get(v,0)+1
        
    def prob(self):
        for (v,w) in self.adjacent.items():
            self.neigh.append(v)
            self.weight.append(w)

    def next_word(self):
        return random.choices(self.neigh, weights= self.weight)[0]


class Graph:
    def __init__(self):
        self.vertice = {}

    def get_vertex_val(self):
        return set(self.vertice.keys())

    def add(self,value):
        self.vertice[value] = vertex(value)

    def get_vertex(self, value):
        if value not in self.vertice:
            self.add(value)
        return self.vertice[value]
    
    def get_next(self, cur):
        return self.vertice[cur.value].next_word()

    def prob_map(self):
        for v in self.vertice.values():
            v.prob()
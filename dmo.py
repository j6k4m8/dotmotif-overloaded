import networkx as nx

class MotifNode:

    def __init__(self, name: str, parent_motif: "MotifCreator"):
        self._parent = parent_motif
        self._name = name
    
    def __rshift__(self, other: "MotifNode") -> "MotifNode":
        self._parent.add_edge(self._name, other._name, {"exists": True})
        return self._parent.get_edge(self._name, other._name)
    
    def __ior__(self, other: "MotifNode"):
        self._parent.add_edge(self._name, other._name, {"exists": False})
        return self._parent.get_edge(self._name, other._name)
    
    def __setitem__(self, key, val):
        self._parent.set_node_attribute(self._name, key, val)

class MotifEdge:

    def __init__(self, u: str, v: str, parent_motif: "MotifCreator"):
        self._u = u
        self._v = v
        self._parent_motif = parent_motif
    
    def __setitem__(self, key, val):
        self._parent_motif.set_edge_attribute(self._u, self._v, key, val)


class MotifCreator:

    def __init__(self):
        self._g = nx.DiGraph()
    
    def add_edge(self, a, b, attrs):
        self._g.add_edge(a, b, **attrs)
    
    def get_edge(self, a, b):
        if self._g.has_edge(a, b):
            return MotifEdge(a, b, parent_motif=self)
    
    def set_edge_attribute(self, u, v, key, val):
        self._g.edges[u, v][key] = val
    
    def set_node_attribute(self, name, key, val):
        self._g.nodes[name][key] = val 
    
    def __getattr__(self, attr):
        if attr in self._g:
            return MotifNode(attr, parent_motif=self)
        else:
            return MotifNode(attr, parent_motif=self)

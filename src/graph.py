from typing import Dict, Tuple, List, Set, Iterable

edge = Tuple[int, int, float]

class Graph:
    def __init__(self, directed: bool = False):
        self.adj: Dict[int, Dict[int, float]] = {}
        self.directed = directed
    
    def add_node(self, u: int):
        self.adj.setdefault(u, {})

    def add_edge(self, u: int, v: int, w: float):
        self.add_node(u)
        self.add_node(v)
        self.adj[u][v] = w 

        if not self.directed:
            self.adj[v][u] = w 
    
    def update_edge(self, u: int, v: int, w: float):
        if u not in self.adj or v not in self.adj:
            raise KeyError(f"Edge {u} - {v} does not exist")
        
        self.adj[u][v] = w 

        if not self.directed:
            self.adj[v][u] = w 

    def remove_edge(self, u: int, v: int):
        if u in self.adj and v in self.adj[u]:
            del self.adj[u][v]
        
        if not self.directed and v in self.adj and u in self.adj[v]:
            del self.adj[v][u]
    
    def neighbors(self, u: int) -> Iterable[Tuple[int, float]]:
        for v, w in self.adj.get(u, {}).items():
            yield v, w 
    
    def nodes(self) -> Set[int]:
        return set(self.adj.keys())
    
    def edges(self) -> List[edge]:
        edges = set()

        for u, nbrs in self.adj.items():
            for v, w in nbrs.items():
                if not self.directed:
                    cur_edge = (*sorted([u, v]), w)
                    if cur_edge in edges:
                        continue
                edges.add((*sorted([u, v]), w))
        
        return list(edges)

    

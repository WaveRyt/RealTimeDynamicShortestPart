from typing import Dict, Tuple, List, Optional
import heapq
from graph import Graph

def dijkstra(graph: Graph, source: int) -> Tuple[Dict[int, float], Dict[int, Optional[int]]]:
    dist = {n: float('inf') for n in graph.nodes()}
    prev = {n: None for n in graph.nodes()}

    if source not in dist:
        return {}, {}
    
    dist[source] = 0 
    hq = [(0, source)]
    
    while hq:
        d, u = heapq.heappop(hq)

        if d > dist[u]:
            continue 

        for v, w in graph.neighbors(u):
            nd = d + w 

            if nd < dist.get(v, float('inf')):
                dist[v] = nd 
                prev[v] = u 
                heapq.heappush(hq, (nd, v))
        
    return dist, prev

class DynamicShortestPath:
    def __init__(self, graph: Graph):
        self.graph = graph
        self._cache: Dict[int, Tuple[Dict[int, float], Dict[int, Optional[int]]]] = {}
    
    def shortest_from(self, source: int):
        if source not in self._cache:
            dist, prev = dijkstra(self.graph, source)
            self._cache[source] = (dist, prev)
    
        return self._cache[source]

    def shortest_path(self, source: int, target: int) -> Tuple[List[int], float]:
        dist, prev = self.shortest_from(source)

        if not dist:
            return [], float('inf')
        
        if dist.get(target, float('inf')) == float('inf'):
            return [], float('inf')

        path = []
        cur = target

        while cur is not None:
            path.append(cur)
            cur = prev[cur]
        
        path.reverse()

        return path, dist[target]
    
    def notify_edge_changed(self):
        self._cache.clear()
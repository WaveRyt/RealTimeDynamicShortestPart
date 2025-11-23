from graph import Graph
from dynamic_dijkstra import DynamicShortestPath

class EventHandler:
    def __init__(self, graph: Graph, dsp: DynamicShortestPath):
        self.graph = graph 
        self.dsp = dsp
    
    def handle(self, line: str) -> str:
        parts = line.strip().split()
    
        if not parts:
            return ""

        cmd = parts[0].upper()

        try:
            if cmd == "ADD" and len(parts) == 4:
                u, v, w = int(parts[1]), int(parts[2]), float(parts[3])
                self.graph.add_edge(u, v, w)
                self.dsp.notify_edge_changed()

                return f"ADDED {u}-{v} weight={w}"
            
            if cmd == "UPDATE" and len(parts) == 4:
                u, v, w = int(parts[1]), int(parts[2]), float(parts[3])
                self.graph.update_edge(u, v, w)
                self.dsp.notify_edge_changed()

                return f"UPDATED {u}-{v} weight={w}"
            
            if cmd == "REMOVE" and len(parts) == 3:
                u, v = int(parts[1]), int(parts[2])
                self.graph.remove_edge(u, v)
                self.dsp.notify_edge_changed()

                return f"REMOVED {u}-{v}"
            
            if cmd == "SHORTEST" and len(parts) == 3:
                s, t = int(parts[1]), int(parts[2])
                path, dist = self.dsp.shortest_path(s, t)

                if not path:
                    return f"NO PATH {s} -> {t}"
                
                return f"Path: {' -> '.join(map(str, path))}, Distance: {dist}"
            
            if cmd == "NODES":
                return "NODES: " + ", ".join(map(str, sorted(self.graph.nodes())))
            
            if cmd == "EDGES":
                return "EDGES: " + ", ".join(f"{u}-{v}:{w}" for u,v,w in self.graph.edges())
            
            return f"UNKNOWN COMMAND or wrong args: {line.strip()}"
        
        except Exception as e:
            return f"ERROR: {e}"

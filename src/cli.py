import sys
from graph import Graph
from dynamic_dijkstra import DynamicShortestPath
from eventhandler import EventHandler

def run():
    g = Graph(directed= False)
    dsp = DynamicShortestPath(g)
    eh = EventHandler(g, dsp)
    print("DynamicRoadNetwork Python CLI.\nCommands: ADD, UPDATE, REMOVE, SHORTEST, NODES, EDGES, QUIT")

    for line in sys.stdin:
        line = line.strip()

        if not line:
            continue
        
        if line.upper() in ("QUIT", "EXIT"):
            print("Exited")
            break

        out = eh.handle(line)

        if out:
            print(out)

if __name__ == "__main__":
    run()
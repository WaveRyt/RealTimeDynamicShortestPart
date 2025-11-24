# Real Time Dynamic Shortest Path 

This is a command-line application for building, modifying, and querying an weighted graph using Dijkstra’s algorithm, with support for dynamic updates to shortest-path results. The program includes an interactive event loop for real-time graph manipulation.

---

## Features
- Add, remove, and update weighted edges in the graph  
- Query shortest-path distances and shortest routes using Dijkstra’s algorithm  
- Automatically recompute shortest paths when the graph changes  
- Simple, modular Python architecture  
- Interactive CLI for real-time experimentation

---

## Files

| File | Description |
|------|-------------|
| `graph.py` | Weighted graph implemented using adjacency lists |
| `dynamic_dijkstra.py` | Dijkstra’s algorithm + dynamic path invalidation mechanism |
| `event_handler.py` | Command parser and event dispatcher |
| `main.py` | Entry point for real-time graph manipulation and shortest-path queries |
| `tests/test.py` | Pytest-based unit tests for shortest path logic |
| `examples/example.txt` | Sample command file for automated input |

---

## Run Instructions

### Interactive Mode
From the project root:

```bash
python src/main.py

---

## Running Tests (pytest)

Ensure pytest is installed:

```bash
pip install pytest
```

Run all tests:

```bash
python -m pytest
```
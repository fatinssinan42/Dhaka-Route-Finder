# Dhaka Route Finder

**CSE 440 Artificial Intelligence, Section 1, Project Group 9, North South University**

Dhaka Route Finder finds the best route between well-known places in Dhaka using search algorithms from the course: **Breadth-First Search (BFS)**, **Uniform Cost Search (UCS)** and **A\* search**. Places are nodes of a weighted graph and main roads are edges. Every road has two costs, distance (km) and travel time (min), so the user can ask for the **shortest** or the **fastest** route, and the two answers are not always the same.

> Status: Week 1. The project structure is set up; the map data and the search algorithms are being added in the coming weeks.

## Planned features

- A map of 18 well-known places in Dhaka (Uttara, Bashundhara, Banani, Gulshan 1, Mohakhali, Farmgate, Dhanmondi 27, Motijheel and more) connected by about 30 main roads
- BFS, UCS and A\* (with a straight-line, haversine heuristic)
- Choice of objective: shortest distance or fastest time
- A traffic toggle that raises the cost of some roads and re-plans the route
- A map drawing that highlights the chosen route
- Experiments comparing the algorithms: path cost, nodes expanded, frontier size and run time

## How to run

Requires Python 3.10 or newer.

```bash
pip install -r requirements.txt
python main.py
```

## Repository structure

| Path | Contents |
|---|---|
| `main.py` | Entry point that runs the project |
| `requirements.txt` | Python libraries the project needs |
| `data/` | Map data: places and roads |
| `support/` | Search algorithms, graph loader, visualisation and experiment code |
| `others/` | Reports, presentation slides and the demo video |

## Team

| Member | ID | Role |
|---|---|---|
| Abdullah Al Galib | 2232535642 | Map data and graph model |
| Pakeezah Tajwar Wafa | 2222115042 | Problem formulation, BFS and UCS |
| Fatin Sadab Sinan | 2233176642 | Coordination, GitHub, A\* and heuristics |
| Nawrose Naomi | 2231306642 | Visualisation, experiments and documentation |

## References

1. CSE 440 Artificial Intelligence lecture notes, Volume 2: Search, North South University.
2. S. Russell and P. Norvig, *Artificial Intelligence: A Modern Approach*, 4th ed., Pearson, 2021.
3. P. E. Hart, N. J. Nilsson and B. Raphael, "A formal basis for the heuristic determination of minimum cost paths," *IEEE Trans. Syst. Sci. Cybern.*, vol. 4, no. 2, pp. 100–107, 1968.

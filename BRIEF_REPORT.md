# Brief Report — AI Campus Route Navigator

**Course:** AI/ML Laboratory, B.Tech. 5th Semester  
**Assignment:** X_03 — AI Campus Route Navigator

## Objective
Build a weighted graph from the CU Technology Campus map and compare Greedy Best-First Search (PATHFINDER) with A* Search (ORBIT).

## Design and implementation
The locations shown on the supplied map are represented as graph nodes. Walkable connections and approximate walking costs are stored separately in `campus.json`. `campus_map.py` loads this data. `search.py` implements both searches using a priority queue; `agents.py` provides the two named agents; `experiment.py` tests five ordinary and CSE-related source/destination pairs and records path, cost, explored nodes and execution time in `results.csv`.

The heuristic uses approximate map coordinates and Manhattan distance. PATHFINDER prioritizes `h(n)`, while ORBIT prioritizes `g(n)+h(n)`. The successor-generation rule restricts CSE entry and exit through Tower 2 Front/Rear Entry and Lift Area.

## Experiments
Run `python main.py` to generate fresh measurements. The five test pairs are:
- Reception of Calcutta University → Library
- Canteen (CU Technology Campus) → New Building 2 (Workshop Building)
- Entry Gate 1 → CSE Laboratory
- Auditorium Hall → CSE_AKC Seminar Hall
- Library → Canteen (CU Technology Campus)

Use the generated `results.csv` as the source for the final comparison. Do not report invented measurements: execution time and explored-node counts depend on the machine and graph.

## Observations / answers
1. **Does Greedy Best-First always find the shortest route?** No. It ranks nodes using only the estimated remaining cost and ignores the cost already travelled, so it can choose a locally promising but more expensive route.
2. **How does A* use distance already travelled?** It adds `g(n)` (cost so far) to `h(n)` (estimated remaining cost) and expands the smallest `f(n)`.
3. **When can the agents choose different paths?** When a route that looks close to the goal has a larger accumulated cost than another alternative; their different priority functions can then expand different nodes.
4. **How does the heuristic affect behaviour?** It guides both searches toward the destination. A misleading or overestimated heuristic can alter route choice and search effort.
5. **What happens under the CSE constraint?** The valid successor set becomes narrower. A route cannot leave a CSE-labelled location directly for an ordinary campus location; it must return to Lift Area and exit through a Tower 2 entry.

## Limitations
The graph's edge costs and coordinate estimates are approximate initial values interpreted from the supplied satellite map. They should be checked against actual campus walkways and the student's campus knowledge. Runtime values are machine-dependent. The program generates the experimental data at execution time.

import heapq
import itertools
import time

CSE = {"CSE Laboratory", "CSE_AKC Seminar Hall", "CSE_Reflxon Room"}
TOWER = {"Tower 2 Front Entry", "Tower 2 Rear Entry"}

def valid_next(current, previous, candidate):
    # Enforce the assignment's CSE entry/exit corridor rule.
    if current in CSE:
        return candidate in CSE or candidate == "Lift Area"
    if current == "Lift Area":
        if previous in CSE:       # exiting the CSE zone
            return candidate in CSE or candidate in TOWER
        if candidate in CSE:      # entering requires coming from a Tower 2 entry
            return previous in TOWER
        if previous in TOWER:     # from Tower entry, Lift may lead into CSE or back out
            return candidate in CSE or candidate in TOWER
        return candidate not in CSE
    if previous in CSE and current in TOWER:
        return candidate == "Lift Area" or candidate in TOWER
    return candidate not in CSE or current == "Lift Area"

def search(campus, start, goal, mode):
    if start not in campus.graph or goal not in campus.graph:
        raise ValueError("Start or destination is not a location in campus.json.")
    if start == goal:
        return {"path":[start], "cost":0, "explored":0, "seconds":0.0}
    counter = itertools.count()
    frontier = [(campus.heuristic(start, goal) if mode=="greedy" else campus.heuristic(start, goal),
                 next(counter), start, None, 0, (start,))]
    best = {}
    explored = 0
    t0 = time.perf_counter()
    while frontier:
        priority, _, node, previous, g, path = heapq.heappop(frontier)
        state = (node, previous if node=="Lift Area" else None)
        if g >= best.get(state, float("inf")):
            continue
        best[state] = g
        explored += 1
        if node == goal:
            return {"path":list(path), "cost":g, "explored":explored,
                    "seconds":time.perf_counter()-t0}
        for nxt, weight in campus.neighbors(node).items():
            if nxt in path or not valid_next(node, previous, nxt):
                continue
            new_g = g + weight
            h = campus.heuristic(nxt, goal)
            score = h if mode=="greedy" else new_g + h
            heapq.heappush(frontier, (score, next(counter), nxt, node, new_g, path+(nxt,)))
    return {"path":[], "cost":None, "explored":explored,
            "seconds":time.perf_counter()-t0}

import csv
from agents import Pathfinder, Orbit

TESTS = [
    ("Reception of Calcutta University", "Library"),
    ("Canteen (CU Technology Campus)", "New Building 2 (Workshop Building)"),
    ("Entry Gate 1", "CSE Laboratory"),
    ("Auditorium Hall", "CSE_AKC Seminar Hall"),
    ("Library", "Canteen (CU Technology Campus)")
]

def run_experiments(campus, output="results.csv"):
    rows = []
    for start, goal in TESTS:
        for agent in (Pathfinder(), Orbit()):
            result = agent.route(campus, start, goal)
            rows.append({
                "start": start, "goal": goal, "agent": agent.name,
                "path": " -> ".join(result["path"]) if result["path"] else "NO ROUTE",
                "cost_m": result["cost"] if result["cost"] is not None else "",
                "nodes_explored": result["explored"],
                "time_seconds": f'{result["seconds"]:.8f}'
            })
    with open(output, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    return rows

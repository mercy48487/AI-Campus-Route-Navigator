from campus_map import CampusMap
from agents import Pathfinder, Orbit
from experiment import run_experiments

def main():
    campus = CampusMap()
    print("\\nAI CAMPUS ROUTE NAVIGATOR")
    print("Available locations:")
    for i, name in enumerate(campus.locations, 1):
        print(f"{i:2}. {name}")
    start = input("\\nEnter starting location (exact name): ").strip()
    goal = input("Enter destination (exact name): ").strip()
    for agent in (Pathfinder(), Orbit()):
        result = agent.route(campus, start, goal)
        print(f"\\n{agent.name}")
        print("Route:", " -> ".join(result["path"]) if result["path"] else "No valid route found")
        print("Cost:", f'{result["cost"]} m' if result["cost"] is not None else "N/A")
        print("Nodes explored:", result["explored"])
        print("Time:", f'{result["seconds"]:.8f} s')
    rows = run_experiments(campus)
    print(f"\\nSaved {len(rows)} experiment records to results.csv")

if __name__ == "__main__":
    main()

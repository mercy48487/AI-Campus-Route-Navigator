import json
from pathlib import Path

class CampusMap:
    def __init__(self, filename="campus.json"):
        data = json.loads(Path(filename).read_text(encoding="utf-8"))
        self.coordinates = data["locations"]
        self.graph = {name: {} for name in self.coordinates}
        for a, b, cost in data["edges"]:
            self.graph[a][b] = cost
            self.graph[b][a] = cost

    @property
    def locations(self):
        return list(self.graph)

    def neighbors(self, location):
        return self.graph[location]

    def heuristic(self, node, goal):
        # Manhattan-distance estimate scaled to the map's approximate walking costs.
        x1, y1 = self.coordinates[node]
        x2, y2 = self.coordinates[goal]
        return 35 * (abs(x1-x2) + abs(y1-y2))

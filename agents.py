from search import search

class Pathfinder:
    name = "PATHFINDER (Greedy Best-First)"
    def route(self, campus, start, goal):
        return search(campus, start, goal, "greedy")

class Orbit:
    name = "ORBIT (A*)"
    def route(self, campus, start, goal):
        return search(campus, start, goal, "astar")

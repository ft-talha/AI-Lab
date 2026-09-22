class RideAgent:
    def __init__(self):
        self.routes = {
            "Fast Route": 7,
            "Safe Route": 9,
            "Cheap Route": 6
        }

    def choose_route(self):
        best_route = max(self.routes, key=self.routes.get)
        return best_route


agent = RideAgent()

route = agent.choose_route()

print("Available routes:")
for name, utility in agent.routes.items():
    print(name, "-> Utility:", utility)

print("Best route:", route)
class GoalBasedAgent:
    def __init__(self):
        self.goal_map = {
            1: "suck the dirt",
            2: "avoid the obstacle",
            3: "clean the spill"
        }
        self.current_state = None

    def perceive(self, loc, state):
        self.current_state = (loc, state)

    def evaluate_goal(self):
        loc, state = self.current_state

        if state in self.goal_map:
            return f"Agent is in location {loc} and {self.goal_map[state]}"
        else:
            return f"Agent is in location {loc} and state is clean"


locations = ['A', 'B', 'C', 'D', 'E']


def get_location(locations):
    location_state = {}

    for loc in locations:
        user_input = int(input(
            f"Enter state for location {loc} (0 for clean, 1 for dirty, 2 for obstacle, 3 for spill): "
        ))

        location_state[loc] = user_input

    return location_state


location_states = get_location(locations)

agent = GoalBasedAgent()

for loc, state in location_states.items():
    agent.perceive(loc, state)
    action = agent.evaluate_goal()
    print(action)
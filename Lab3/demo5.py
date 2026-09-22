class UtilityBasedAgent:
    def __init__(self):
        self.utilities = {
            "clean_dirt": 10,     
            "avoid_obstacle": 7, 
            "clean_spill": 8,     
            "no_action": 0       
        }

    def perceive(self, loc, state):
        self.current_state = (loc, state)

    def choose_action(self):
        loc, state = self.current_state

        if state == 1:   
            action = "clean_dirt"
        elif state == 2:  
            action = "avoid_obstacle"
        elif state == 3:  
            action = "clean_spill"
        else:              
            action = "no_action"

        return f"At {loc}: Perform {action} (Utility = {self.utilities[action]})"


locations = {"A": 1, "B": 2, "C": 0, "D": 3}

agent = UtilityBasedAgent()

for loc, state in locations.items():
    agent.perceive(loc, state)      
    print(agent.choose_action())     
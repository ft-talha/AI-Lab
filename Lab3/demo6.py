import random


class LearningAgent:

    def __init__(self):
        self.knowledge = {
            "clean_dirt": 5,
            "avoid_obstacle": 3,
            "clean_spill": 4,
            "no_action": 0,
        }

    def perceive(self, loc, state):
        self.current_state = (loc, state)

    def choose_action(self):
        return random.choice(list(self.knowledge.keys()))

    def learn(self, action, reward):
        self.knowledge[action] += reward
        print(f"Updated knowledge: {action} -> {self.knowledge[action]}")


agent = LearningAgent()

feedback = {
    "clean_dirt": 10,  
    "avoid_obstacle": 7,  
    "clean_spill": 8,  
    "no_action": -2, 
}

for i in range(5):
    print(f"\n--- Iteration {i+1} ---")

    action = agent.choose_action()
    print(f"Agent chose: {action}")

    reward = feedback[action]
    print(f"Environment reward: {reward}")

    agent.learn(action, reward)
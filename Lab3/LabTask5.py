class TicTacToeAI_LA:
    def __init__(self):
        self.knowledge = {}

    def update_knowledge(self, state, move, outcome):
        if state not in self.knowledge:
            self.knowledge[state] = {}
        
        reward = 10 if outcome == "win" else -5
        self.knowledge[state][move] = self.knowledge[state].get(move, 0) + reward

ai = TicTacToeAI_LA()

print("Game 1: AI Move = Random")
ai.update_knowledge("State1", "Move(2,2)", "win")

print("Game 2: AI Learns winning move at position (2,2)")
print(f"Knowledge: {ai.knowledge}")
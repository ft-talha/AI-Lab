class MazeAgent:
    def __init__(self):
        self.room_memory = {}

    def perceive(self, room, treasure):
        if room not in self.room_memory:
            self.room_memory[room] = "visited"

            if treasure == "yes":
                return f"Room {room}: Treasure found, pick it up"
            else:
                return f"Room {room}: Unvisited, explore"
        else:
            if treasure == "yes":
                return f"Room {room}: Treasure found, pick it up"
            else:
                return f"Room {room}: Already visited, avoid"


agent = MazeAgent()

for i in range(3):
    room = input(f"Enter room {i + 1}: ")
    treasure = input("Treasure found? (yes/no): ").lower()

    action = agent.perceive(room, treasure)

    print(action)
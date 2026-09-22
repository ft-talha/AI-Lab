class RescueRobot:
    def __init__(self):
        self.goal = "Victim"

    def choose_action(self, location, options):
        if self.goal in options:
            return f"Robot moves from {location} to Victim"
        else:
            return f"Robot moves from {location} to {options[0]}"


robot = RescueRobot()

location = "Base"

options = ["Street"]
action = robot.choose_action(location, options)
print(action)

location = "Street"

options = ["Building"]
action = robot.choose_action(location, options)
print(action)

location = "Building"

options = ["Victim"]
action = robot.choose_action(location, options)
print(action)
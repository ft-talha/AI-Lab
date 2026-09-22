class modelbasdagent:
  def __init__(self, locations):
    self.internal_model= { loc: 0 for loc in locations}

  def preceive(self , loc,state=None):
    if state is not None:
      self.internal_model[loc]=state
      
  def select_action(self, loc):
    state = self.internal_model.get(loc, 0)                     
    if state==1:
      return f"Agent is in location {loc} and suck the dirt"
    elif state==2:
      return f"Agent is in location {loc} and avoid the obstacle"
    elif state==3:
      return f"Agent is in location {loc} and clean the spill"
    else:
     return f"Agent is in location {loc} and state is clean"

def get_location(locations):
    location_state={}
    for loc in locations:
        user_input=input(f"Enter state for location {loc} (0 for clean, 1 for dirty, 2 for obstacle, 3 for spill): ")

        if user_input.strip() =="":
            location_state[loc]=0
        else:
            location_state[loc]=int(user_input)
    return location_state

locations = ['A', 'B', 'C', 'D', 'E']
agent = modelbasdagent(locations)

print("FIRST ROUND")
location_state = get_location(locations)

for loc, state in location_state.items():
    agent.preceive(loc, state)
    action = agent.select_action(loc)
    print(action)

print("\nSECOND ROUND")
location_state = get_location(locations)

for loc, state in location_state.items():
    agent.preceive(loc, state)
    action = agent.select_action(loc)
    print(action)
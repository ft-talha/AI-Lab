def input_percept(loc, state):
  rule_match(loc, state)

def rule_match(loc, state):
    if state==1:
        print(f"Agent is in location {loc} and suck the dirt")
    elif state==2:
        print(f"Agent is in location {loc} and avoid the obstacle")
    elif state==3:
        print(f"Agent is in location {loc} and clean the spill")
    else:
        print(f"Agent is in location {loc} and do nothing")

# main

loc= input("enter location A, B, C, D or E:").upper()

print("enter state (0 for clean, 1 for dirty, 2 for obstacle, 3 for spill):")
state = int(input())

input_percept(loc, state)
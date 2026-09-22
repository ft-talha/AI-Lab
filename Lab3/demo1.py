import random

def random_agent():
    precept()

def precept():
    loc= input("enter location A or B:")

    state=int(input("enter state 0 or 1:"))
    action= action_rule(loc , state)

    print_action(action)

def action_rule(loc, state):
     actions=['Clean', 'Left', 'Right', 'No Action']

     return random.choice(actions)

def print_action(action):
    if action =='Right':
        print("Agent moves to the right")
    elif action=='Left':
        print("Agent moves to the left")
    elif action=='Clean':
        print("Agent cleans the current location")
    elif action == 'No Action':
        print("Agent does nothing")

# main
print("Welcome to program")

random_agent()

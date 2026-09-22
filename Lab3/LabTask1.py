def climate_agent(temp):
    if temp < 20:
        return "Heater ON"
    elif temp > 28:
        return "AC ON"
    else:
        return "System OFF"


for i in range(3):
    temp = float(input(f"Enter room temperature {i + 1}: "))
    action = climate_agent(temp)
    print(action)
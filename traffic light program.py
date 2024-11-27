def traffic_light(action):
    switcher={
            "red":"stop",
            "yellow":"ready",
            "green":"go"
            
            }
    return switcher.get(action,"invalid command")
print(traffic_light("red"))
print(traffic_light("orange"))

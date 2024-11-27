def traffic_light(action):
    switcher={
            "red":'stop',
            "Yellow":'Slow Down',
            "Green":'Go'
            }
    return switcher.get(action,"Invalid action")
print(traffic_light("red"))
print(traffic_light("Yellow"))
print(traffic_light("Green"))
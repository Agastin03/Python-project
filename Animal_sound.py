def animal_sound(animal):
    switcher={
            "bark":'Dog',
            "meow":'Cat',
            "moo":'Cow',
            "roar":'Lion',
            }
    return switcher.get(animal,"Unknown Sound")
print(animal_sound("bark"))
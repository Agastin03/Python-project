def animal_sound(animal):
    switcher={
            'dog':'bark',
            'cat':'meow',
            'lion':'roar',
            }
    return switcher.get(animal,"unknown sound")
print(animal_sound('train'))
print(animal_sound('lion'))
    
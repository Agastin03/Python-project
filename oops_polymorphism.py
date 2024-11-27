class Animal:
    def sound(self):
        print("some genetic animal sound")
class Dog(Animal):
    def sound(self):
        print("Bark")
class Cat(Animal):
    def sound(self):
        print("meow")
animals=[Animal(),Dog(),Cat()]
for animal in animals:
    animal.sound()
                    
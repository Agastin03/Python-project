class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f"Hello,my name is {self.name} and I am {self.age} years old.")
personal=person("alice",30)
personal.greet()
class student(person):
        def __init__(self,name,age,student_id):
            super().__init__(name,age)
            self.student_id=student_id
        def display_id(self):
            print(f"My student ID is {self.student_id}")
student1=student("Bob",20,"S12345")
student1.greet()
student1.display_id()
            
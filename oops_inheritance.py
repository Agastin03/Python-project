class student(person):
    def __init__(self,name,age,student_id):
        super()._init__(name,age)
        self.student_id=student_id
    def display_id(self):
        print(f"My student ID is {self.student_id}.")
    student1=student("Bob",20,"S123")
    student1.display_id()    
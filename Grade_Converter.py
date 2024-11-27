def grade_to_gpa (grade):
    switcher= {
            4:'A',
            3:'B',
            2:'C',
            1:'D',
            0:'F'
            }
    return switcher.get (grade,"Invalid grade")
print(grade_to_gpa(4))

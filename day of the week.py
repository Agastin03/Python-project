def day_of_the_week(day_number):
    switcher ={
            1:"sunday:",
            2:"monday:",
            3:"tuesday:",
            4:"Wednesday:",
            5:"Thursday:",
            6:"friday:",
            7:"saturday:",                
                }
    return switcher.get(day_number,"Invalid day number")
print(day_of_the_week(1))
print(day_of_the_week(8))
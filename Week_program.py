def day_week (day_number):
    switcher={
            1:"Sunday",
            2:"Monday",
            3:"Tuesday",
            4:"Wednesday",
            5:"Thursday",
            6:"Friday",
            7:"Saturday"
            }
    return switcher.get(day_number,"Invalid day")
print(day_week(1))
print(day_week(8))
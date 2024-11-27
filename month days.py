def days_in_month(month):
    switcher={
            'January':31,
            'february':28,
            'march':31,
            'april':30,
            'may':31,
            'june':30,
            'August':31,
            'september':30,
            'octomber':31,
            'november':30,
            'december':31,          
            }
    return switcher.get(month,"Invalid Month")
print(days_in_month('february'))
print(days_in_month('april'))
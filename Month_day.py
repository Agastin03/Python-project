def days_in_month(month):
    switcher={
            31:'January',
            28:'februray',
            31:'March',
            30:'April',
            31:'May',
            30:'June',
            31:'July',
            31:'August',
            30:'September',
            31:'October',
            30:'Novmber',
            31:'December'
            }
    return switcher.get(month,"Invalid Month")
print(days_in_month(28))
#month=int(input("Enter a Month Days "))
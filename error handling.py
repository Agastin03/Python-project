try:
    a=int(input("enter the number:"))
    b=int(input("enter the another number:"))
    result=a/b
    print("result:",{result})
except ZeroDivisionError:
    print("error:Division by zero is not allowesd")
except ValueError:
    print("error:Invalid input,please enter a number")
    
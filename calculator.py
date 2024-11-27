def Calculator (operation , num1, num2):
    switcher={
            'add': num1 + num2,
            'sub': num1 -num2,
            'mul' : num1* num2,
            'div' : num1/num2 if num2 !=0 else 'Error: Division by zero'
            }
    return switcher.get(operation,'Invalid operation')
print(Calculator('add',10,5))
print(Calculator('sub',10,5))
print(Calculator('mul',10,5))
print(Calculator('div',10,5))
def shape_area(shape,dimension):
    if(shape=='Circle'):
        return 3.14*(dimension**2)
    elif(shape=='Square'):
        return dimension**2
    elif(shape=='triangle'):
        return 0.5*dimension[0]*dimension[1]
    else:
        return"Invalid Shape"
print(shape_area('Circle',5))
print(shape_area('Square',4))
print(shape_area('triangle',(3,4)))
print(shape_area('hexagonal',5))
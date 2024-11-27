def temperature_converter(scale,temperture):
    if(scale=='C to F'):
        return (temperture*9/5)+32
    elif(scale=='f to c'):
        return (temperture-32)*5/9
    else:
        return "Invalid Scale"
print(temperature_converter('C to F',0))
print(temperature_converter('f to c',32))
print(temperature_converter('C to k',0))
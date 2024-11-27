def temperature_convertor(scale,temp):
    if scale=="c_to_f":
        return(temp*9/5)+32
    elif scale=="f_to_c":
        return(temp-32)*5/9
    else:
        return("invalid scale")

print(temperature_convertor("c_to_f",0))
print(temperature_convertor("f_to_c",0))
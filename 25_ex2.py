TEMP=float(input('Enter temperature:'))
choice=input('Is this is in Celsius(C) or Fahrenheit(F)?')
if choice=='C':
    f=(9/5*TEMP)+32
    print(TEMP,'Celsius is',f,'Fahrenheit')
else:
    c=5/9(TEMP-32)
    print(TEMP,'Fahrenheit is',c,'Celsius')
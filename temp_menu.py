while True:
    print('1. \tConvert Celsius to Farenheit')
    print('2. \tConvert Farenheit to Celsius')
    print('3. \tExit')
    ch=int(input('Enter your choice:'))
    if ch==1:
        TEMP_C=float(input('Enter a temperature in Celsius:'))
        f=(TEMP_C*9/5)+32
        print(TEMP_C,'C=',f,'Farenheit')
    elif ch==2:
        TEMP_F=float(input('Enter a temperature in Celsius:'))
        c=(TEMP_F-32)*5/9
        print(TEMP_F,'F=',c,'Celsius')
    else:
        break
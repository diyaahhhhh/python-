num1=int(input('Enter a number:'))
num2=int(input('Enter another number:'))
num3=int(input('Enter another number:'))
large=0
if num1>num2 and num1>num3:
    large=num1
elif num2>num1 and num2>num3:
    large=num2
else:
    large=num3
print('The largest number is:',large)
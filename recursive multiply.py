def multiply(num1,num2):
    if num1==0 or num2==0:
        return 0
    else:
         return num1+(multiply(num1,num2-1))
num1=int(input('Enter a number:'))
num2=int(input('Enter another number:'))
print(multiply(num1,num2))
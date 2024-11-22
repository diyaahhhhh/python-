user=[]
even=[]
odd=[]
n=int(input('How many digits you want to enter?'))
for i in range(n):
    num=int(input('Enter a digit:'))
    user.append(num)
user.sort()
merged_list=[]
for i in user:
     if i%2==0:
        even.append(i)
     else:
         odd.append(i)
merged_list.extend(odd)
print('Even:',even)
print('Odd:',odd)
print('Before sorting:',user)
print('Sorted list:',merged_list)




list1=[]
list2=[]
merged_list=[]
n=int(input('Enter the number of elements:'))
for i in range(n):
    num=int(input('Enter a number:'))
    list1.append(num)
even=[]
for i in list1:
    if i%2==0:
        even.append(i)
    else:
        list2.append(i)
    even.sort()
    list2.sort()
merged_list.extend(even)
merged_list.extend(list2)
print('List:',list1)
print('Even:',even)
print('Odd:',list2)
print('After sorting:',merged_list)
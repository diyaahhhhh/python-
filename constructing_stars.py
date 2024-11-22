#Increasing triangle
'''row=int(input('Enter the number of rows'))
for i in range(1,row+1):
    for j in range(i):
        print('*',end='\t')
    print()

#Decreasing triangle
row1=int(input('Enter the number of rows:'))
for k in range(row1,0,-1):
    for l in range(k):
        print('*', end='\t')
    print()

#Hill pattern
row2=int(input('Enter the number of rows:'))
for i in range(1,row2+1):
    for j in range(row2-i):
        print(' ',end='\t')
    for k in range(2*i-1):
        print('*',end='\t')
    print()'''

#Reverse hill
row3=int(input('Enter the number of rows:'))
for i in range(row3,0,-1):
    for j in range(row3-i):
        print(' ',end='\t')
    for k in range(2*i-1):
        print('*',end='\t')
    print()
import math #i need some of maths functions
data=''
i=0#declares i
title=input('Enter a title for the data:')
print('')
print('You entered:',title)
print()
col_1=input('Enter the column 1 header:\n')#1st column
print('You entered:',col_1)
print()
col_2=input('Enter the column 2 header:\n')#second column
print('You entered:',col_2)
print()
data_point=input('Enter a data point (-1 to stop input):\n')
data=data.split(',')
print()
print('%33s'%title)#formats the title
print('%-20s|%23s'%(col_1,col_2))#formats the columns
print('-'*44)#makes the horizontal line
for points in range(0,(len(data)-math.ceil((len(data)/2)))):#subtracting the data divided by 2 and rounding up prevents index errors
    print('%-20s|%23s'%(data[i],data[i+1]))#inputs the data
    i=i+2z
i=0
print()

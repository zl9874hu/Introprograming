data=''
i=1#because i  cant figure out how to format the chart
title=input('Enter a title for the data:')
print('')
print('You entered:',title)
print()
col_1=input('Enter the column 1 header:\n')
print('You entered:',col_1)
print()
col_2=input('Enter the column 2 header:\n')
print('You entered:',col_2)
print()
data_point=input('Enter a data point (-1 to stop input):\n')
while data_point != '-1':
    d=data_point.split(',')
    if len(d) >1:
        d[1]=d[1].replace(' ','')
    if len(d) == 1:
        print('Error: No comma in string.\n')
    elif len(d) >= 3:
        print('Error: Too many commas in input.\n')
    elif d[1].isdigit() != True:
        print('Error: Comma not followed by an integer.\n')
    else:
        print('Data string:',d[0])
        print('Data integer:',d[1])
        print()
        data+=('%s$'%data_point)
    data_point=input('Enter a data point (-1 to stop input):\n')
print(data)
data=data.replace('$',',')
data=data.split(',')
print(data)
print()
print('%33s'%title)
print('%-20s|%23s'%(col_1,col_2))
print('-'*44)
for points in range(0,len(data),2):
    print('%-20s|%23s'%(data[i],data[i+1]))
    i=i+2
i=1
for points in range(0,len(data),2):
    print('%20s'%data[i+1],('*'*int(data[i])))
    i+=2

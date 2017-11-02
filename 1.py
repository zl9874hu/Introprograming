def monthly_rainfall():
    i=1
    rainfall=[]
    while i <= 12:#iterates 12 times
        rain=int(input('Enter the ranfall for month %d: '%i))
        rainfall.append(rain)
        i+=1
    return rainfall
def rainfall_stats(rainfall):
    tot_rainfall=sum(rainfall)#adds the list
    avg_rainfall=tot_rainfall/12
    high_rainfall=max(rainfall)#finds highest element in list
    high_month=rainfall.index(high_rainfall)#finds the index of the element in the list
    low_rainfall=min(rainfall)
    low_month=rainfall.index(low_rainfall)
    return tot_rainfall,avg_rainfall,high_rainfall,high_month,low_rainfall,low_month
rainfall=monthly_rainfall()#sets rainfall to the return of montly_rainfall
tot_rainfall,avg_rainfall,high_rainfall,high_month,low_rainfall,low_month=rainfall_stats(rainfall)#unpacks rainfall_stats
rainfall_stats(rainfall)
print('It rainedd',tot_rainfall,'inches this year')
print('The average rainfall was',avg_rainfall,'inches')
print('It rained the most on month',(high_month+1),'with',high_rainfall,'inches.')#plus 1 is neccasary to have the right month not index number
print('It rained the least on month',(low_month+1),'with',low_rainfall,'inches.')

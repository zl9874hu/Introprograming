months=['January','Febuary','March','April','May','June','July','Augest','September','October','November','December']
def monthly_rainfall():
    i=0#set this to 0 to start at january
    rainfall=[]
    while i <=11:#11 because we start at 0
        rain=int(input('Enter the ranfall for %s'%months[i]))
        rainfall.append(rain)
        i+=1
    return rainfall#make sure this is in line with the function not the loop
def rainfall_stats(rainfall):
    tot_rainfall=sum(rainfall)
    avg_rainfall=tot_rainfall/12
    high_rainfall=max(rainfall)
    high_month=months[rainfall.index(high_rainfall)]#gets the name of the month
    low_rainfall=min(rainfall)
    low_month=months[rainfall.index(low_rainfall)]
    return tot_rainfall,avg_rainfall,high_rainfall,high_month,low_rainfall,low_month
rainfall=monthly_rainfall()
tot_rainfall,avg_rainfall,high_rainfall,high_month,low_rainfall,low_month=rainfall_stats(rainfall)
rainfall_stats(rainfall)
print('It rained',tot_rainfall,'inches this year')
print('The average rainfall was',avg_rainfall,'inches')
print('It rained the most on month',(high_month),'with',high_rainfall,'inches.')#plus 1 is neccasary to have the right month not index number
print('It rained the least on month',(low_month),'with',low_rainfall,'inches.')
#no longer need the +1

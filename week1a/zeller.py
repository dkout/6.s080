year=2017
month=1
day=9
y=year
m=month
d=day
if m==1 or m==2: 
	y1=y-1
	m1=m+12
else:
	y1=y
	m1=m
y2=y1%100
c=y1//100
w=(d+(13*(m1+1))//5+y2+y2//4+c//4-2*c)%7
print(w)

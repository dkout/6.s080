interest_rate = 0.2
if interest_rate==0:
    print("NEVER")
else:
    x=1
    count=0
    while x<2:
        x=x*(1+interest_rate)
        count+=1
    print(count)

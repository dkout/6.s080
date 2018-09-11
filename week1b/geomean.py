numbers=[1,2,3,4,5]
if len(numbers)==0:
    print('None')
else:
    avg=1
    for i in numbers:
        avg=avg*i
    avg=avg**(1/(len(numbers)))
    print(avg)

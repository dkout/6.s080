numbers=[1,2,3,4,5]
if len(numbers)==0:
    print('None')
else:
    avg=0
    for i in numbers:
        avg+=i
    avg=avg/(len(numbers))
    print(avg)

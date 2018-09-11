
def second_largest_number(numlist):
    if len(numlist)<=2:
        return None
    largest=0
    largest2=0
    for i in numlist:
        if i > largest:
            largest2=largest
            largest=i
        if i > largest2 and i <largest:
            largest2=i
    return largest2


       


def prime(x):
    if x==2:
        return True
    if x%2==0 or x==0 or x==1:  
        return False
    for i in range(2,x):
        if x%i==0:
            return False
        
    return True


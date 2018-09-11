
def ndoors(n):
    doors=[False]*n
    for i in range(1,n+1):
        for x in range(i, n+1,i):
            doors[x-1]=not doors[x-1]

#print (doors)
    ans=[]
    for i in range(len(doors)):
        if doors[i]==True:
            ans.append(i+1)
    return(ans)

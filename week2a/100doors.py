

doors=[False]*100
for i in range(1,101):
    for x in range(i, 101,i):
         doors[x-1]=not doors[x-1]

print (doors)
ans=[]
for i in range(len(doors)):
    if doors[i]==True:
        ans.append(i+1)
print(ans)

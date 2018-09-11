p_d=1111
r=p_d/2
s=int(r)

inside=0
out=0
for x in range(-s, s+1):
    for y in range(-s,s+1):

        if x**2+y**2<=r**2:
            inside+=1
        else:
            out+=1
pi=4*inside/p_d**2
print(pi)

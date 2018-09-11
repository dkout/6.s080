side=2
spacing=0.2
flowerd=0.2
graveld=0.2
pi=3.14159265358979
r=side/4

carea=pi*r**2
scarea=carea/2
scplants=scarea//(spacing**2)
cplants=carea//(spacing**2)
print ("Flowers in Semi-Circle: ", scplants, "\nFlowers in Circle: ", cplants, "\nTotal flowers: ", 4*scplants+cplants, "\n\n")
scsoil=scarea*flowerd/27
csoil=carea*flowerd/27
print("Semi Circle soil volume: ", scsoil, "\nCircle soil volume: ", csoil, "\nTotal soil volume: ", 4*scsoil+csoil, "\n**In cubic yards**\n\n")
grarea=side**2-3*carea
gravel=grarea*graveld/27
print("Total Gravel volume in cubic *yards*: ", gravel)


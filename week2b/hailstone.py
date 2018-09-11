def hailstone_sequence(a_0):
    vals=[a_0]
    val=a_0
    while val !=1:
        if val%2==0:
            val=val/2
        else:
            val=3*val+1
        vals.append(val)
    return vals

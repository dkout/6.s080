def run_langton(rules,size):
    import math
    orientation=0
    directions={0:(0,1),1:(1,0),2:(0,-1),3:(-1,0)}
    x,y=(size)//2,math.ceil(size/2)-1
    ncolors=len(rules)
    grid=[[0]*(size) for i in range(size)]
    count=0
    #print (x,y)
    while max(x,y)<size and min (x,y)>=0:
        count+=1
        grid[y][x]=(grid[y][x]+1)%ncolors
        x+=directions[orientation][0]
        y+=directions[orientation][1]
        if max(x,y)>=size or min (x,y)<0:
            break
        turn=rules[grid[y][x]]
        if turn=='R':
            orientation=(orientation+1)%4
        else:
            orientation=(orientation-1)%4
        #print(turn, orientation, (x,y), grid)


    grid.reverse()
    return (count, grid)

toppings=['bacon', 'anchovies']
size='medium'
cost=0
if size=='small':
    cost=14
if size=='medium':
    cost=16
if size=='large':
    cost=18
cost=cost*(1+len(toppings)*0.1)
if 'bacon' in toppings or 'anchovies' in toppings:
    cost+=5

print (cost)


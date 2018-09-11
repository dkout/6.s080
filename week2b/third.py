
def tokenize(input_string):
    out=[]
    last=0
    if len(input_string)==0:
        return input_string
    for i in range(len(input_string)):
        if input_string[i]==' ':
            out.append(input_string[last:i])
            last=i+1
    if input_string[-1]!=' ':
        out.append(input_string[last:i+1])
    return out

def number_check(x):
    digits='0123456789.'
    for i in x:
        if i not in digits:
            return False
        if i =='.':
            digits='0123456789'
    return True

def evaluate(expression, stack, binary_operations={'+': lambda x,y: x+y,'*': lambda x,y: x*y,'MAX': max,'-': lambda x,y: x-y}, unary_operations={'DOUBLE': lambda x: x*2, 'ABS': abs}, variables={}):
    for exp in tokenize(expression):

        if exp=='PRINT':
            print(stack)

        if exp=='STORE':
            variables[stack.pop()]=stack.pop()

        if exp=='LOAD':
            loadvar=stack.pop()
            if loadvar not in variables:
                print('Cannot find variable')
                break
            else:
                stack.append(variables[loadvar])
        if number_check(exp):
            stack.append(float(exp))
        if exp in unary_operations:
            if len(stack)<1:
                print('stack too small')
                break
            stack.append(unary_operations[exp](stack.pop()))
        elif exp in binary_operations:
            if len(stack)<2:
                print('stack too small')
                break
            stack.append(binary_operations[exp](stack.pop(-2),stack.pop()))

    userin=input('Next Input: ')
    if userin != 'QUIT':
        evaluate(userin, stack, binary_operations, unary_operations, variables)

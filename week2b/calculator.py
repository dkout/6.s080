
def tokenize(input_string): 
    out=[]
    last=0
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

def evaluate(expression, stack, binary_operations, unary_operations):
    for exp in tokenize(expression):
       
        if number_check(exp):
            stack.append(float(exp))
        elif exp in unary_operations:    
            stack.append(unary_operations[exp](stack.pop()))
        elif exp in binary_operations:
            stack.append(binary_operations[exp](stack.pop(-2),stack.pop()))
        print('stack: ', stack)




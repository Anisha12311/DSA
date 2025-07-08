def expression(tokens):
    
    precedence = {'+' : 1, '-': 1, '*' : 2, '/' : 2}
    
    output = []
    stack = []
    
    for token in tokens:
        if token.isalnum():
            output.append(token)
            
            
        elif token in precedence:
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence[token]:
                output.append(stack.pop())
                
            stack.append(token)
            
        elif token == '(':
            stack.append(token)
            
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        
    while stack:
        output.append(stack.pop())
    
    return output
 
 
def evaluate(tokens):
    
    stack = []
    
    for token in tokens:
        
        if token.isnumeric():
            stack.append(int(token))
            
        else:
            a = stack.pop()
            b = stack.pop()
            
            if token == '+': stack.append(a+b)
            if token == '-' : stack.append(a-b)
            if token == '*': stack.append(a*b)
            if token == '/' :stack.append(a//b)
            
    return stack
    
expr = ['(', '3', '+', '4', ')', '*', '2']
print("Postfix:", expression(expr))
token = expression(expr)

print(evaluate(token))
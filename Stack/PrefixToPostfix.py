import math
char = 'A*B-(C+D+F)+E'
# output = 'AB*CD+-E+'

def isEmpty(stack):
    return len(stack) == 0

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}  
    stack = []
    output = []
    
    for char in expression:
        if char.isalnum():  # If it's an operand (A-Z, 0-9), add to output
            output.append(char)
        
        elif char == '(':  
            stack.append(char)  # Push '(' to stack
        
        elif char == ')':  
            while stack and stack[-1] != '(':
                output.append(stack.pop())  # Pop until '('
            stack.pop()  # Remove '(' from stack
        
        else:  # If it's an operator (+, -, *, /, ^)
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence.get(char, 0):
                output.append(stack.pop())  # Pop operators with higher precedence
            stack.append(char)

    while stack:  # Pop all remaining operators in the stack
        output.append(stack.pop())

    return "".join(output)

# Example input
expression = "A*B-(C+D/F)+E"
postfix_expression = infix_to_postfix(expression)
print("Postfix Expression:", postfix_expression)


value = '123*+5-'

def Postfix(txt):
    stack = []
    for char in txt:

        if char.isdigit():
            stack.append(int(char))
        else:
            first = stack.pop()
            second = stack.pop()
            match(char):
                case '+' : 
                    value = second + first
                    stack.append(value)
                case '-':
                    value = second - first
                    stack.append(value)
                case '*':
                    value = second * first
                    stack.append(value)
                case '/':
                    value = second / first
                    stack.append(value)
            print(value, "value")
            
    return stack         

    
print(Postfix(value))   



value1 = '100 * ( 2 + 12 ) / 14'
out = 100


def Infix(txt) : 
    operand = []
    operator = []
    word = txt.split(" ")
    for char in word:
        
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}  

        if char.isdigit():
            operand.append(int(char))
            
        elif char == '(':
            operator.append(char)
        elif char == ')':
            while operator and operator[-1] != '(':
                value = operator.pop()
                
                first = operand.pop()
                second = operand.pop()
                
                match(value):
                    case '+' : 
                        value = second + first
                        operand.append(value)
                    case '-':
                        value = second - first
                        operand.append(value)
                    case '*':
                        value = second * first
                        operand.append(value)
                    case '/':
                        value = second / first
                        operand.append(value)
            operator.pop()
        else:
            while operator and  operator[-1] != '(' and precedence.get(operator[-1],0) >= precedence.get(char, 0):
                value = operator.pop()
                
                first = operand.pop()
                second = operand.pop()
                
                match(value):
                    case '+' : 
                        value = second + first
                        operand.append(value)
                    case '-':
                        value = second - first
                        operand.append(value)
                    case '*':
                        value = second * first
                        operand.append(value)
                    case '/':
                        value = second / first
                        operand.append(value)
            
            operator.append(char)
        if len(operand) <= 1:
            return operand[0]
        
        while operator:
            
            value = operator.pop()
                
            first = operand.pop()
            second = operand.pop()
            
            match(value):
                case '+' : 
                    value = second + first
                    operand.append(value)
                case '-':
                    value = second - first
                    operand.append(value)
                case '*':
                    value = second * first
                    operand.append(value)
                case '/':
                    value = second / first
                    operand.append(value)
        if len(operand) != 1:
            raise ValueError("Invalid expression: Too many operands left after evaluation.")

    return "".join(operand)


print(Infix(value1))
            
            
value2 = '-+7*45+20' 

def split_expression(value): 
    result = []
    num = ""
    
    for char in value:
        if char.isdigit():
            num += char
            
        else:
            if num:
                result.append(num)
                num = ""
            result.append(char)
            
    if num:
        result.append(num)   
    return result    

def prefix(txt):
    stack = []
    reverseDigit = txt[::-1]
    print(reverseDigit)
    operator = set('+-/*')
    print(reverseDigit)
    for char in reverseDigit:
        if char.isdigit():
            stack.append(int(char))
            
        elif  len(stack) > 1 :     
            first = stack.pop()
            second = stack.pop()
            match(char):
                case '+' : 
                    value = second + first
                    stack.append(value)
                case '-':
                    value =abs(second - first)
                    stack.append(value)
                case '*':
                    value = second * first
                    stack.append(value)
                case '/':
                    value = second / first
                    stack.append(value)
    return stack       
    
print(prefix(value2))



def palidrome_Str(str):
    
    split_str = str.split('X')
    
    return split_str[0][::-1] == split_str[1]
    
    
    
print(palidrome_Str('abababXbababa'))
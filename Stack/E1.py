import math

# Valid Parentheses in an Expression

s = "[()]{}{[()()]()}"
s1 = "[(])"
def isPair(s):
    
    stack = []
    
    for char in s:
        print(char)
        if char in '([{':
            stack.append(char)
            
        elif char in ')]}':
            
            if not stack:
                print(stack)
                return False
            
            top = stack.pop()
            
            if (top == '(' and char != ')') or (top == '{' and char != '}') or (top == '[' and char != ']'):
                print("stack",stack)
                return False
    
    print(stack)        
            
    return len(stack) == 0


if isPair(s1):
    print("true")
    
else :
    print("False")
    
    
    
# Reverse the string


str = "GeeksQuiz"

def reverseStr(str):
    stack = []
    
    for char in str:
        
        stack.append(char)
        
    return "".join(stack[::-1])
    
print(reverseStr(str))


# Remove string


string1 = "occurrence"
string2 = "car"


def removeString(s1,s2):
    str1 = ""
    stack2 = []
    
    for sub in s2:
        stack2.append(sub)
        
    for char in s1:
        
        if char not in stack2:
            str1 += char
        
            
    print(str1)
    
removeString(string1, string2)



# Delete middle element


st1 = [1, 2, 3, 4, 5]

def deleteMiddle(st):
    
    middle = len(st)//2
    
    del st[middle]
    
    print("str", st)
    
deleteMiddle(st1)

# Reverse Word

word = 'Hello World'

def reverse_word(word):
    stack = word.split(' ')
    str = ""
    for w in stack:
        str += w[::-1]
        str += " "
    print(str)
    
reverse_word(word)


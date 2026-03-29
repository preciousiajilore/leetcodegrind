def validParentheses(s:str) -> bool: 
    """
    This returns True if it is a valid parentheses and False, otherwise
    """
    stack=[]
    brackets ={
        "[" : "]",
        "(" : ")",
        "{" : "}"
    }
    for char in s:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack:
                return False
            
            opening = stack.pop()
            if brackets[opening] != char:
                return False
        else:
            continue
            
    return len(stack) == 0
 
def main():
    s = "({[y]})"
    t = "(("
    print(validParentheses(s))
    print(validParentheses(t))

if __name__ == "__main__":
    main()

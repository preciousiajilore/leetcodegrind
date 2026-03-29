def candyCrush(s:str, k:int) -> str: 
    stack = []
    for char in s:
        if stack and stack[-1][0] == char:
            stack[-1][1] += 1
        else:
            stack.append([char,1])
        
        if stack[-1][1] == k:
            stack.pop()
    
    result = []
    for char, count in stack:
        result.append(char * count)
    return "".join(result)

def main():
    s = "deeedbbcccbdaa"
    print(candyCrush(s, 3))

if __name__ == "__main__":
    main()
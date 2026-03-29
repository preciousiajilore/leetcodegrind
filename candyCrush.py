def candyCrush(s:str, k:int) -> str: 
    stack = []
    for char in s:
        if not stack:
            stack.append([char, 1])
            continue
        
        current = stack[-1]

        #print(current)
        if current[0] == char:
            current[1] += 1

            if current[1] == k:
                #print("popping")
                #print(current)
                stack.pop()

        else:
            stack.append([char, 1])
    
    result = []
    for char, count in stack:
        result.append(char * count)
    return "".join(result)

def main():
    s = "deeedbbcccbdaa"
    print(candyCrush(s, 3))

if __name__ == "__main__":
    main()
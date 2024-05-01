def check_brackets(s: str) -> str:
    stack = list()
    output = list()
    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        elif ch == ')':
            if len(stack) == 0:
                output.append('?')
                continue
            else:
                stack.pop()
        output.append(' ')
    for i in stack:
        output[i] = 'x'
    return ''.join(output)



def main():
    while True:
        s = input()
        print(check_brackets(s))

if __name__ == "__main__":
    main()
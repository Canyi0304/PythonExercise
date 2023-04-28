row_input = int(input())

for _ in range(row_input):
    stack = []
    vps = True
    for ch in input():
        if ch == '(':
            stack.append(ch)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                vps = False
                break
    # more than 1 line
    if len(stack) > 0:
        vps = False

    print("YES" if vps else "NO")
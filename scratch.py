sample = 'baabs'
stack = []

for s in sample:
    if stack and s == stack[-1]:
        stack.pop()
    else:
        stack.append(s)

output = "".join(stack)

print(output)

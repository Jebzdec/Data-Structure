normal, mirror = input("Enter Input (Normal, Mirror) : ").split()
stack = []
queue = []

mirror = list(reversed(mirror))
cnt = 0
while not mirror == []:
    top = mirror.pop()
    if top == stack[-1]:
        cnt += 1
    else:
        cnt = 0

    stack.append(top)

    if cnt == 3:
        for i in range(3):
            stack.pop()
        cnt = 0

print(stack)

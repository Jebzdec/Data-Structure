normal, mirror = input("Enter Input (Normal, Mirror) : ").split()
stack = []
items = []

mirror = list(mirror)
normal = list(normal)
size_items = 0
while not mirror == []:
    top = mirror.pop()
    if len(stack) < 2:
        stack.append(top)
    else:
        # print(*stack, sep='', end=' ')
        # print(stack[-2], stack[-1], top)
        if stack[-1] == stack[-2] and stack[-1] == top:
            stack.pop()
            stack.pop()
            items.append(top)
            size_items += 1
        else:
            stack.append(top)
            

normQ = []
cnt_exp = 0
fail_intr = 0
while not normal == []:
    top = normal.pop(0)
    if len(normQ) < 2:
        normQ.append(top)
    else:
        #print(*normQ, ' -> ', top)
        if normQ[-1] == normQ[-2] and normQ[-1] == top:
            if items != []:
                if items[0] == top:
                    items.pop(0)
                    normQ.pop()
                    fail_intr += 1
                else:
                    normQ.append(items.pop(0))
                    normQ.append(top)

            else:
                normQ.pop()
                normQ.pop()
                cnt_exp += 1
        else:
            normQ.append(top)

print('NORMAL : ')
print(len(normQ))
if len(normQ) > 0:
    print(*reversed(normQ), sep='')
else:
    print('Empty')
print(f'{cnt_exp} Explosive(s) ! ! ! (NORMAL)')
if fail_intr > 0:
    print(f'Failed Interrupted {fail_intr} Bomb(s)')
print('------------MIRROR------------')
print(': RORRIM')
print(len(stack))
if len(stack) > 0:
    print(*reversed(stack), sep='')
else:
    print('ytpmE')
print(f'(RORRIM) ! ! ! (s)evisolpxE {size_items}')

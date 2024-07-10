inp = input('Enter Input : ').split('/')
wi = list(map(int, inp[0].split()))
max_cnt = int(inp[1])
sum = 0
for e in wi:
    sum += e

bf_boxw = 0
left = 0
right = sum
box_w = 0
ans = 0
while True:
    if left > right:
        print(f'Minimum weigth for {max_cnt} box(es) = {ans}')
        break
    use = True
    box_w = int((left+right)/2)
    cnt = 1
    sum_w = 0
    for e in wi:
        if sum_w+e > box_w:
            cnt += 1
            sum_w = 0
        if e > box_w or cnt > max_cnt:
            use = False
            break
        sum_w += e
        # print('round ', sum_w, cnt, e)
    # print(box_w, use)
    if use == False:
        left = box_w+1
    else:
        ans = box_w
        right = box_w-1

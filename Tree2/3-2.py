inp = input('Enter Input : ').split('/')
inp[0] = int(inp[0])
inp[1] = list(map(int, inp[1].split()))
size = len(inp[1])
if size*2-1 != inp[0]:
    print('Incorrect Input')
else:
    sum = 0
    while len(inp[1]) != 1:
        n = len(inp[1])
        new = []
        Min = inp[1][0]
        idx = 0
        cnt = 0
        for i in range(n):
            if inp[1][i] < Min:
                idx = i
                Min = inp[1][i]

            cnt += 1

            # print(inp[1][i], cnt, Min, sum)
            # print(cnt == 2)
            if cnt == 2:
                sum += inp[1][i]-Min + inp[1][i-1]-Min
                new.append(Min)
                cnt = 0
                Min = float('inf')

            if i == n-1 and cnt == 1:
                last = new.pop()
                if last > inp[1][i]:
                    Min = inp[1][i]
                else:
                    Min = last
                sum += inp[1][i]-Min + last-Min
                new.append(Min)

        inp[1] = new
    sum += inp[1][0]
    print(sum)

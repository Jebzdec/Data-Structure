print("Enter All Bid : ",end='')
List = list(map(int,input().split()))
x = max(List)
n = len(List)
for i in range(n):
    if i==0 :
        fst = List[i]
        idf = i
    elif List[i]>=fst:
        sec = fst
        fst = List[i]
        ids = idf
        idf = i
    elif List[i]>=sec:
        sec = List[i]
        ids = i

if i<2:
    print("not enough bidder")
elif :
    
#pair sort

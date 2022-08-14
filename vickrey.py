bid = []
bid = list(map(int, input("Enter All Bid : ").split()))
bid.sort()
if bid[-1] == bid[0]:
    print("not enough bidder")
elif bid[-1] == bid[-2]:
    print("error : have more than one highest bid")
else:
    print(f'winner bid is {bid[-1]} need to pay {bid[-2]}')

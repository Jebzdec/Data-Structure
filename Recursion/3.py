max_len = 0


def func(n):
    global max_len
    if n < 0:
        print("Only Positive & Zero Number ! ! !")
        return 0
    b = bin(n)[2:]
    if len(b) > max_len:
        max_len = len(b)
    if n > 0:
        func(n-1)

    print(b.zfill(max_len))


inp = int(input("Enter Number : "))
func(2**inp - 1)

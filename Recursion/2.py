def length(txt):
    txt = txt[1:]
    if txt != '':
        k = 1+length(txt)
        print('*' if k % 2 == 1 else '~', end='')
        print(txt[0], end='')
        return k
    else:
        return 1


print("\n", length(input("Enter Input : ")), sep="")

# ~

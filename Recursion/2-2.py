def length(txt):
    #print('*' if k % 2 == 1 else '~', end='')
    # txt = txt[1:]
    if txt != '':
        print(k)
        print(txt[0], end='')
        k = 1+length(txt[1:])
        return k
    else:
        return 0


print("\n", length(input("Enter Input : ")), sep="")

# ~

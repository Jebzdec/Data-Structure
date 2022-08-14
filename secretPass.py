#s = input("Enter secret code : ")
def bon(w):
    return ord(w)-ord('a')+1

secretCode = input("Enter secret code : ")
for i in secretCode:
    if secretCode.count(i)>1 :
        print(bon(i)*4)
        break

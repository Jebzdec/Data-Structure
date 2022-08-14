def bon(w):
    Sum=0
    for i in range(len(w)):
        Sum+=ord(w[i])
	
    return Sum

secretCode = input("Enter secret code : ")
print(bon(secretCode))
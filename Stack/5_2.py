
max_height = -1
cnt = 0

def find(key,value):
    if key=='A':
        if value< max_height:
            cnt += 1
            max_height = value
        
    elif key=='B':

Input = input("Enter Input : ").split(',')
for i in Input:
    try:
        k,h = i.split()
    except:
        k = i[0]
    
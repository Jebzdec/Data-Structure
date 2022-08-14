from socket import if_nametoindex


print("*** Converting hh.mm.ss to seconds ***")
print("Enter hh mm ss : ",end='')
h,m,s = map(int,input().split())
if m<0 or m>=60:
    print("mm(%d) is invalid!"%(m))
elif s<0 or s>=60:
    print("ss(%d) is invalid!"%(s))
elif h<0 or h>23:
    print("hh(%d) is invalid!"%(h))
else:
    sec = "{:,}".format(h*3600 + m*60 + s)
    if(h<10):
        h = '0'+str(h)
    if(m<10):
        m = '0'+str(m)
    if(s<10):
        s = '0'+str(s)
    print("%s:%s:%s = %s seconds"%(h,m,s,sec))
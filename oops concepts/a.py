s=[]
a=[5,8,9,0,66,18]
for i in range(1,len(a)):
    if (a[i]%2==0 and a[i-1]%3==0):
        s.append(a[i]/2)
    else:
        s.append(a[i]*2)
print(s)
a = [6,1,3,5,6,3,1]
r=[]
i=0
while i<len(a):
    if a[i] not in r:
        r.append(a[i])
        b=a[i]*i
    i=i+1
print(r)
print(b*4)


#2)))
thislist = (("apple", "banana", "cherry"))
print(list(thislist))

##3))...
thislist = (list(("apple", "banana", "cherry")))
print(thislist)
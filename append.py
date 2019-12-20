a=[1,2,3,4,5,6]
c=[12,11,13,14,1,16]
b=input("enter list b=")
for i in range(0,len(a)):
    b.append(a[i])
print "a=",a
print "afte appending new list is:",b
for i in range(0,len(c)):
    if(c[i]%2==1):
        a.append(c[i])
print "odd numbers are appended to list a:",a

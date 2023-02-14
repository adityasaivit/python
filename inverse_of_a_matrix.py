t=int(input("ENTER THE INDEX:"))
l=[]
for i in range(t):
    l1=input().split(" ")
    l.append(l1)
print(l)
lf=[]
l2=[]
l3=[]
for k in range(1,len(l)+1,1):
    l2.clear()
    for m in range(1,len(l)+1,1):
        l2.append(l[m-1][k-1])
    l3=l2.copy()
    lf.append(l3)
print()
print()
for x in lf:
    for y in x:
        print(y,end=" ")
    print()
from math import sqrt
l=[0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,700]
n=len(l)
m=int(sqrt(n))
flag,found,key=0,0,700

for i in range(0,n,m):
    if l[i]==key:
        print "using jump search found at index ",i
        flag,found=1,1
        break
    elif l[i]>key:
        flag=1
        break

#valid block found
if not found and flag and i!=0:
    for j in range(i-m,i):
        if l[j]==key:
            print "using jump search found at index ",j
            found=1

#check for last block
if not flag:
    for j in range(i+1,n):
        if l[j]==key:
            print "using jump sort found at index ",j
            found=1

if not found:
    print "Element not present in list",count
             

    




    



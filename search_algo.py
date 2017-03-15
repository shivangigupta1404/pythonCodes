from math import sqrt

def linear_search(list,key):
    for i in range(len(list)):
        if list[i]==key:
            return i
    return -1
        
def binary_search(l,key):
    list=l[:]
    list.sort()
    print "sorted list used in binary search : ",list
    l,r=0,len(list)-1
    while l<=r:
        mid=(l+r)/2
        if list[mid]==key:
            return mid
        elif list[mid]<key:
            l=mid+1
        else:
            r=mid-1
    return -1

def jump_search(l,key):
    list=l[:]
    list.sort()
    print "sorted list used in jump search : ",list
    n=len(list)
    m=int(sqrt(n))
    flag,found=0,0
    for i in range(0,n,m):
        if l[i]==key:
            return i
        elif l[i]>key:
            flag=1
            break

    #valid block found
    if flag and i!=0:
        pos=linear_search(list[i-m:i],key)
        if pos!=-1:
            return i-m+pos
        return pos

    #check for last block
    if not flag:
        pos=linear_search(list[i+1:],key)
        if pos!=-1:
            return i+1+pos
        return pos
        
def exp_search(l,key):
    list=l[:]
    list.sort()
    print "sorted list used in exponential search : ",list
    i,found=1,0
    if list[0]==key:
        return 0
    while i<len(list) and list[i]<=key:
        i*=2
    if i>=len(list):
        return -1
    if list[i]==key:
        return i
    else:
        pos=binary_search(list[i/2:i],key)
        if pos!=-1:
            return (i/2)+pos
        return pos
        
def ternary_search(l,key):
    list=l[:]
    list.sort()
    print "sorted list used in ternary search : ",list
    l,r=0,len(list)-1
    while l<=r:
        mid1=l+(r-l)/3
        mid2=l+(2*(r-l))/3
        print "mid1 is : ",mid1," mid2 is : ",mid2," list under consideration : ",list[l:r+1]
        if list[mid1]==key:
            return mid1
        if list[mid2]==key:
            return mid2
        if key<list[mid1]:
            r=mid1-1
        if key>list[mid1] and key<list[mid2]:
            l=mid1+1
            r=mid2-1
        if key>list[mid2]:
            l=mid2+1
    return -1


            

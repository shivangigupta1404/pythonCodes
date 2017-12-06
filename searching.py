from search_algo import *

arr=(raw_input("Enter the array space separated : ")).strip().split(" ")
n=len(arr)
for i in range(n):
    arr[i]=int(arr[i])
print arr
choice='y'
while choice=='y' or choice=='Y':
    print "Searching Menu"
    print "1. Linear Search "
    print "2. Binary Search "
    print "3. Jump Search"
    print "4. Exponential Search"
    print "5. Ternary Search"
    ch=raw_input("Enter your choice (1-5) : ")
    key=int(raw_input("Enter the element to be searched : "))
    if ch=='1':
        pos=linear_search(arr,key)
        if pos==-1:
            print "Used Linear Search and The element is not found in the list"
        else:
            print "Used Linear Search and The element is found at index ",pos
    elif ch=='2':
        pos=binary_search(arr,key)
        if pos==-1:
            print "Used Binary Search and The element is not found in the list"
        else:
            print "Used Binary Search and The element is found at index ",pos
    elif ch=='3':
        pos=jump_search(arr,key)
        if pos==-1:
            print "Used Jump Search and The element is not found in the list"
        else:
            print "Used Jump Search and The element is found at index ",pos
    elif ch=='4':
        pos=exp_search(arr,key)
        if pos==-1:
            print "Used Exponential Search and The element is not found in the list"
        else:
            print "Used Exponential Search and The element is found at index ",pos
    elif ch=='5':
        pos=ternary_search(arr,key)
        if pos==-1:
            print "Used Ternary Search and The element is not found in the list"
        else:
            print "Used Ternary Search and The element is found at index ",pos
    else:
        print "Not a valid choice"
    choice=raw_input("Do you want to continue? (y/n) : ")



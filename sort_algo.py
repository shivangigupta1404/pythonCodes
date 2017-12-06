def selection_sort(arr):
    n=len(arr)
    for i in range(0,n-1):
        print arr
        small=arr[i]
        pos=i
        for j in range(i+1,n):
            if arr[j]<small:
                small=arr[j]
                pos=j
        if pos!=i:
            arr[pos]=arr[i]
            arr[i]=small
    print arr
        

def bubble_sort(arr):
    n=len(arr)
    for i in range(0,n-1):
        print arr
        swap=0
        for j in range(1,n-i):
            if arr[j-1]>arr[j]:
                swap=1
                temp=arr[j]
                arr[j]=arr[j-1]
                arr[j-1]=temp
        #Sorting can be optimised by stopping the algorithm if inner loop does not cause any swap
        if not swap:
            break
    print arr
        

def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        print arr
        element=arr[i]
        j=i-1
        while j>=0:
            if arr[j]>element:
                arr[j+1]=arr[j]
            else:
                break
            j=j-1
        arr[j+1]=element
    print arr


            
            
            

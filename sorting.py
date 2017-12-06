from sort_algo import *

choice='y'
while choice=='y' or choice=='Y':
    print "Soring Menu"
    print "1. Selection Sort "
    print "2. Bubble Sort"
    print "3. Insertion Sort"
    ch=raw_input("Enter your choice (1-3) : ")
    arr=raw_input("Enter the space separated list of elements to be sorted : ").strip().split(" ")
    if ch=='1':
        selection_sort(arr)
        print "Sorted elements using Selection Sort. List becomes "," ".join(arr)
    elif ch=='2':
        bubble_sort(arr)
        print "Sorted elements using Bubble Sort. List becomes "," ".join(arr)
    elif ch=='3':
        insertion_sort(arr)
        print "Sorted elements using Insertion Sort. List becomes "," ".join(arr)
    else:
        print "Not a valid choice"
    choice=raw_input("Do you want to continue? (y/n) : ")


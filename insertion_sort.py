def insertion_sort(list1):
    for i in range(1,len(list1)):
        tempt=list1[i]
        j=i-1
        while j>=0 and tempt<list1[j]:
            list1[j+1]=list1[j]
            j=j-1
        list1[j+1]=tempt
    return list1
list1=[10,5,13,8,2]
print("The Unsorted list is:",list1)
print("The sorter list1 is:",insertion_sort(list1))
        
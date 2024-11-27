def selection_sort(array):
    length=len(array)
    for i in range(length-1):
        minindex=i
        for j in range(i+1,length):
            if array[j]<array[minindex]:
                minindex=j
                array[i],array[minindex]=array[minindex],array[i]
        return array
array=[21,6,9,33,3]
print("The Sorted array is :",selection_sort(array))

def quicksort(arr,lo,hi):
    if lo<hi:
        p=partition(arr,lo,hi)
        quicksort(arr,lo,p-1)
        quicksort(arr,p+1,hi)
def partition(arr,lo,hi):
    pivot=arr[hi]
    i=lo-1
    for j in range(lo,hi):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[j]
    arr[i+1],arr[hi]=arr[hi],arr[i+1]
    return i+1
arr=[10,7,8,9,1,5]
n=len(arr)
quicksort(arr,0,n-1)
print("sorted array:",arr)

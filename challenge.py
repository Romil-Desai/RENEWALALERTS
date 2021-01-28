arr=[102,5,7,6,0,50,float("inf")]
def partition(arr,low,high):
    pivot=arr[low]
    i=low
    j=high
    while(j>i):
        while(pivot<=arr[i]):
            i=i+1
        while(pivot>arr[j]):
            j=j-1
        if(i<j):
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j
def quicksort(arr,low,high):
    if(low<high):
        j=partition(arr,low,high)
        print(j)
        print(arr[low:j])
        quicksort(arr,low,j)
        print(arr[j+1:high])
        quicksort(arr,j+1,high)
quicksort(arr,0,len(arr)-1)
print(arr)







# divide and conquer bajanir ev tirir

arr = [1,8,9,3,7,6,4]

#partition function ov gtnum enq pivoti indexy vekalelov pivoty paymanakanorena menaverjin tarry u berum
# enq en index i vra voric dzax sax tarrery iranic poqr en isk aj sax mec en u kirarum enq arden quicksort
# function y mi hat pivotic dzaxi vra mi hatel dranic aji vra
def partition(arr,low,high): # low=0 high = 6
    i = low - 1
    pivot = arr[high]

    for j in range(low,high):
        if arr[j]<=pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1
#print(partition(arr,0,len(arr)-1))

def quicksort(arr,low,high):
    if low<high:
        pi = partition(arr,low,high)  # veradardznuma partitionic heto pivoti indexy
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)

def sort_arr(arr):
    quicksort(arr,0,len(arr)-1)
    return arr

print(sort_arr(arr))
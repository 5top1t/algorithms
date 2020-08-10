'''

Merge sort 
algorithm: 
__divide on conquer algorithm. Each recursive call to merge chooses the middle element
    and recursively calls sort of the left and right half. There are log(n) recursive call on average
__After each recursive call, a linear amount of work is done to merge to two halves

Runtime average: O(n*log(n)) if the array is shuffled
Runtime worst case: O(n^(2)) if the array is sorted in reverse
Space complexity O(n)

'''

def mergesort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    L = arr[0:mid]
    R = arr[mid:]

    mergesort(L)
    mergesort(R)

    i = j = k = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
            k += 1
        else:
            arr[k] = R[j]
            j += 1
            k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
        



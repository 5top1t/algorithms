'''

Quick sort 
algorithm: 
__divide on conquer algorithm. After placing a pivot in the correct position,
    where every element less than pivot is to the left and every element greater than the
    pivot is to the right. Recursive call quick sort on element left of the 
    pivot and the element right of the pivot.
__Best implemented with two methods one to partition one to recurse
__Work is done in partition place elements less than the pivot to the left of its occuring index
__Each iteration will put the greatest element of the unsorted array to its write position

Runtime average: O(n*log(n)) if the array is shuffled
Runtime worst case: O(n^(2)) if the array is sorted in reverse
Space: O(1) a.k.a in place

'''
import random #optimizaton


def quicksort(arr, low, high):
    if low < high:
        # place pivot
        p = pivot(arr, low, high)
        quicksort(arr, low, p-1)
        quicksort(arr, p+1, high)

def pivot(arr, low, high):
    # choose right most as pivot
    p_val = arr[high]

    # pivot is assumed to be rightmost
    # comfirm all elements to the right
    # less the the pivot, i + 1 represents
    # the final position for this pivot
    i = low - 1

    for j in range(low, high):
        if arr[j] < p_val:
            i += 1 # smaller element now occupies this index
            arr[i] , arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1





# __________________________________Optimization__________________________________________
#random.shuffle(arr)
#_______________________add to cheats on how to shuffle an array__________________________
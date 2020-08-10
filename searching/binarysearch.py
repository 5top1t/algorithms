'''
binary search 
algorithm: 
__Assuming the array is sorted. Check the middle element recursively
    call binary search on the left and right sides of mid.

Runtime: O(log(n)
Space: O(1) a.k.a in place
'''

# assumes arr is sorted
# return -1 is val is not found
def binarysearch(arr, low, high, val):
    if low <= high:
        mid = (high + low) // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] > val:
            return binarysearch(arr, low, mid-1, val)
        else:
            return binarysearch(arr, mid+1, high, val)
    return -1

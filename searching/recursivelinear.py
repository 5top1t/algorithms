'''
recursive linear search 
algorithm: 
__Assuming the array is sorted. Recursively check elements at the
    beginning and ending elements of the array.
__Shift low and high index in each call

Runtime: O(n)
Space: O(1) a.k.a in place
'''

def recursivelinearsearch(arr, low, high, val):
    if low <= high:
        if arr[low] == val:
            return low
        if arr[high] == val:
            return high
        return recursivelinearsearch(arr, low+1, high-1, val)
    return -1


""" 
arr = [1, 2, 3, 4, 5, 6, 7, 8]
print(recursivelinearsearch(arr, 0, len(arr)-1, 4)) 
"""
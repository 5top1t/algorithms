'''

Selection sort 
algorithm: 
__Loop through assuming the elements to the left of our index are sorted.
__We maintain the sorting by swaping the least in the unsorted right to the left.
__Work is done to find the least value in the list of unsorted iteration.
__Faster than bubble sort on most list due to less swapping.
__Performs O(N) swaps

Runtime: O(n^(2))
Space: O(1) a.k.a in place
Stable: Yes. Not does not swap equivalent elements.

'''

def selectionsort(arr):
    if len(arr) < 2:
        return

    for i in range(len(arr)):
        
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
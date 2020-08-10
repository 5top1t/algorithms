'''
Insertion sort 
algorithm: 
__Loop through assuming the elements to the left of our index are sorted.
__We maintain the sorting by swaping elements leftwards into the ordered position.
__Work is done to shuffle each input element in the right positon as they are encounter. 
    AKA. Does not look for the least element.
__Faster than bubble and selection in practice. Quick on small list.
__Performs N^2 swaps

Runtime: O(n^(2))
Space: O(1) a.k.a in place
Stable: Yes. Does not change the order of equivalent elements.

'''

def insertionsort(arr):
    if len(arr) < 2:
        return

    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1






    
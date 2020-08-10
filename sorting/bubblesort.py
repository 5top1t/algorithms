'''

bubble sort 
algorithm: 
__Loop through the arr looking at two elements at a time. Sorts 
    in descendin order putting the greatest element in the right most position.
__We swap is the element to the left > element to the right
__Each iteration will put the greatest element of the unsorted array to the 
    right most position

Runtime: O(n^(2))
Space: O(1) a.k.a in place
Stable: Yes. Does not change the order of equivalent elements.

Optimization: Stop the algorithm if no swaps happen in an iteration.
'''

def bubblesort(arr):
    if len(arr) < 2:
        return

    for i in range(len(arr)):
        #isSorted = True

        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                isSorted = False
        """ if isSorted:
            break """

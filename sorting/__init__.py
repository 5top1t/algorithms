import time
import random
from insertionsort import insertionsort
from selectionsort import selectionsort
from bubblesort import bubblesort
from quicksort import quicksort
from mergesort import mergesort

test = [[34,16, 66, 54, 99, 74, 58, 24, 46, 37, 82, 93, 8, 65, 81, 42, 85, 88, 57,
57, 11, 14, 94, 33, 68, 55, 70, 60, 1, 64, 26, 90, 37, 44, 47, 58, 97,
30, 41, 43, 79, 12, 91, 92, 39, 20, 89, 11, 98, 59, 54, 80, 29, 26, 46,
69, 44, 45, 47, 33, 38, 53, 99, 19, 25, 12, 50, 64, 34, 54, 75, 22, 77,
98, 29, 10, 86, 47, 83, 63, 54, 6, 27, 61, 2, 57, 77, 23, 89, 7, 24,
32, 88, 51, 79, 44, 75, 12, 90, 83, 7, 46, 2, 35, 23, 93, 26, 24, 57,
32, 75, 18, 33, 19, 57, 47, 6, 17, 92, 85, 34, 56, 14, 24, 96, 8, 52,
11, 5, 8, 72, 34, 70, 28, 98, 81, 89, 9, 21, 86, 90, 82, 73, 3, 83,
53, 85, 37, 12, 80, 28, 29, 2, 46, 95, 87, 69, 44, 41, 91, 17, 4, 56,
51, 54, 35, 32, 79, 75, 91, 2, 81, 67, 10, 29, 92, 99, 90, 65, 69, 53],
[34,16, 66, 54, 99, 74, 58, 24, 46, 37, 82, 93, 8, 65, 81, 42, 85, 88, 57,
57, 11, 14, 94, 33, 68, 55, 70, 60, 1, 64, 26, 90, 37, 44, 47, 58, 97,
30, 41, 43, 79, 12, 91, 92, 39, 20, 89, 11, 98, 59, 54, 80, 29, 26, 46,
69, 44, 45, 47, 33, 38, 53, 99, 19, 25, 12, 50, 64, 34, 54, 75, 22, 77,
98, 29, 10, 86, 47, 83, 63, 54, 6, 27, 61, 2, 57, 77, 23, 89, 7, 24,
32, 88, 51, 79, 44, 75, 12, 90, 83, 7, 46, 2, 35, 23, 93, 26, 24, 57,
32, 75, 18, 33, 19, 57, 47, 6, 17, 92, 85, 34, 56, 14, 24, 96, 8, 52,
11, 5, 8, 72, 34, 70, 28, 98, 81, 89, 9, 21, 86, 90, 82, 73, 3, 83,
53, 85, 37, 12, 80, 28, 29, 2, 46, 95, 87, 69, 44, 41, 91, 17, 4, 56,
51, 54, 35, 32, 79, 75, 91, 2, 81, 67, 10, 29, 92, 99, 90, 65, 69, 53],
[34,16, 66, 54, 99, 74, 58, 24, 46, 37, 82, 93, 8, 65, 81, 42, 85, 88, 57,
57, 11, 14, 94, 33, 68, 55, 70, 60, 1, 64, 26, 90, 37, 44, 47, 58, 97,
30, 41, 43, 79, 12, 91, 92, 39, 20, 89, 11, 98, 59, 54, 80, 29, 26, 46,
69, 44, 45, 47, 33, 38, 53, 99, 19, 25, 12, 50, 64, 34, 54, 75, 22, 77,
98, 29, 10, 86, 47, 83, 63, 54, 6, 27, 61, 2, 57, 77, 23, 89, 7, 24,
32, 88, 51, 79, 44, 75, 12, 90, 83, 7, 46, 2, 35, 23, 93, 26, 24, 57,
32, 75, 18, 33, 19, 57, 47, 6, 17, 92, 85, 34, 56, 14, 24, 96, 8, 52,
11, 5, 8, 72, 34, 70, 28, 98, 81, 89, 9, 21, 86, 90, 82, 73, 3, 83,
53, 85, 37, 12, 80, 28, 29, 2, 46, 95, 87, 69, 44, 41, 91, 17, 4, 56,
51, 54, 35, 32, 79, 75, 91, 2, 81, 67, 10, 29, 92, 99, 90, 65, 69, 53],
[34,16, 66, 54, 99, 74, 58, 24, 46, 37, 82, 93, 8, 65, 81, 42, 85, 88, 57,
57, 11, 14, 94, 33, 68, 55, 70, 60, 1, 64, 26, 90, 37, 44, 47, 58, 97,
30, 41, 43, 79, 12, 91, 92, 39, 20, 89, 11, 98, 59, 54, 80, 29, 26, 46,
69, 44, 45, 47, 33, 38, 53, 99, 19, 25, 12, 50, 64, 34, 54, 75, 22, 77,
98, 29, 10, 86, 47, 83, 63, 54, 6, 27, 61, 2, 57, 77, 23, 89, 7, 24,
32, 88, 51, 79, 44, 75, 12, 90, 83, 7, 46, 2, 35, 23, 93, 26, 24, 57,
32, 75, 18, 33, 19, 57, 47, 6, 17, 92, 85, 34, 56, 14, 24, 96, 8, 52,
11, 5, 8, 72, 34, 70, 28, 98, 81, 89, 9, 21, 86, 90, 82, 73, 3, 83,
53, 85, 37, 12, 80, 28, 29, 2, 46, 95, 87, 69, 44, 41, 91, 17, 4, 56,
51, 54, 35, 32, 79, 75, 91, 2, 81, 67, 10, 29, 92, 99, 90, 65, 69, 53]]

sorting_algs = ["insertionsort: ", "bubblesort: ", "selectionsort: ", "quicksort: ", "mergesort: "]

# insertion sort
start = time.time()
for testcase in test:
    random.shuffle(testcase)
    insertionsort(testcase)
runtime = time.time() - start
print('{} {}'.format(sorting_algs[0], runtime*10000))

# selection sort
start = time.time()
for testcase in test:
    random.shuffle(testcase)
    selectionsort(testcase)
runtime = time.time() - start
print('{} {}'.format(sorting_algs[2], runtime*10000))

# bubble sort
start = time.time()
for testcase in test:
    random.shuffle(testcase)
    bubblesort(testcase)
runtime = time.time() - start
print('{} {}'.format(sorting_algs[1], runtime*10000))

# quick sort
start = time.time()
for testcase in test:
    random.shuffle(testcase)
    quicksort(testcase, 0, len(testcase)-1)
runtime = time.time() - start
print('{} {}'.format(sorting_algs[3], runtime*10000)) # note: uncomment random.shuffle in qs to improve runtime

# merge sort
start = time.time()
for testcase in test:
    random.shuffle(testcase)
    mergesort(testcase)
runtime = time.time() - start
print('{} {}'.format(sorting_algs[4], runtime*10000))

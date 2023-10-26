import random

'''Quick Sorting Algorithm Practice'''

def test():
    test = []
    while len(test) < 15: test.append(random.randint(0,50))
    if len(test) == 15: return test
#print(test())

"""======================================================================"""

'''Recursive Quicksort'''
def quickSort(items, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(items) - 1

    print('Range for quickSort()', items[left:right + 1])
    print('...The full list is:', items)

    if left >= right:
        return
    
    # start partition
    i = left
    pivotVal = items[right]

    print(f'.....The pivotVal is {pivotVal}')

    for j in range(left, right):
        if items[j] <= pivotVal:
            items[i], items[j] = items[j], items[i]
            i += 1
    items[i], items[right] = items[right], items[i]
    # end partition

    print('..........After swapping, the range is:', items[left:right + 1])
    print('Recursively calling quicksort on:',
           items[left:i], 'and ', items[i+1:right+1])
    
    # run quick sort on each half of partition 
    quickSort(items, left, i - 1)
    quickSort(items, i + 1, right)

items = test()
quickSort(items) 
print("Final list is: \n", items)

"""======================================================================"""

'''Iterative QuickSort Algorithm'''
def partition(arg, low, high):
    
    i = (low - 1)
    pivot = arg[high]

    for j in range(low, high):
        if arg[j] <= pivot:
            i += 1
            arg[i], arg[j] = arg[j], arg[i]

    arg[i + 1], arg[high] = arg[high], arg[i + 1]
    print('Creating partition, pivot value is: ', pivot)
    return (i + 1)

def iterQuickSort(arg, low, high):

    if low < high:
        pi = partition(arg, low, high)

        iterQuickSort(arg, low, pi -1)
        iterQuickSort(arg, pi+1, high)

    print('QuickSorting Iteratively on:', arg)

arg = test()
n = len(arg)
iterQuickSort(arg, 0, n-1)
print('Final: ',arg)
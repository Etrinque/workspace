import random
#
'''Sorting Algorithm Practice'''

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
def iterativeQuickSort():
    pass
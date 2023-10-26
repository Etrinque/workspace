import math
import time

start_time = time.time()

'''Merge-Sort Algorithm Practice'''

testList = [2,4,7,1,8,0,6,9,3,5,-1,-2,-3,-4,-5,-6,-7,-8,-9,]

'''RECURSIVE MERGE-SORT'''

def mergeSort(arg):

    print("MergeSort called on: ", arg)

    if len(arg) == 0 or len(arg) == 1:
        return arg
    
    midPoint = math.floor(len(arg) / 2)

    print("Split into 2 halve: ", arg[:midPoint], 'and', arg[midPoint:])
    print("The midPointer index is: ", midPoint)

    left = mergeSort(arg[:midPoint])
    right = mergeSort(arg[midPoint:])

    resultList = []
    iLeft = 0
    iRight = 0

    while len(resultList) < len(arg):
        if left[iLeft] < right[iRight]:
            resultList.append(left[iLeft])
            iLeft += 1
        else:
            resultList.append(right[iRight])
            iRight += 1

        if iLeft == len(left):
            resultList.extend(right[iRight:])
            break
        elif iRight == len(right):
            resultList.extend(left[iLeft:])
            break
    print("Two halves merged into: ", resultList)
    return resultList

testList = mergeSort(testList)
print(testList)

print("Process finished --- %s seconds ---" % (time.time() - start_time))

import random

"""Binary search algorithm practice file with tests"""

def test():
    test = []
    while len(test) < 30:
        test.append(random.randint(0,51))
    if len(test) == 30:
        return test

"""======================================================================"""

'''Recursive'''
def binarySearch(needle, haystack, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(haystack)-1
    
    if left > right:
        return None
    
    mid = (left + right) // 2
    if needle == haystack[mid]:
        return mid
    elif needle < haystack[mid]:
        return binarySearch(needle, haystack, left, mid - 1)
    elif needle > haystack[mid]:
        return binarySearch(needle, haystack, mid + 1, right)

needle = random.randint(1,50)
arg = test()
print(f"Recursively searching for {needle}: in haystack, "f"{binarySearch(needle, arg)}", arg)

"""======================================================================"""

'''Itterative'''
def iterativeBinarySearch(needle, haystack, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(haystack) - 1

    while left < right:
        mid = (left + right) // 2 

        if haystack[mid] == needle:
            return mid

        elif haystack[mid] < needle:
            left = mid + 1
        else:
            right = mid - 1
    return None

needle = random.randint(1,50)
haystack = test()

print(f"Iteratively searching for {needle}: in haystack, "
       f"{iterativeBinarySearch(needle, haystack)}", haystack)
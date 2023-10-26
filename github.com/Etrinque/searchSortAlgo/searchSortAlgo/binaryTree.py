class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d 
b.right = e
c.right = f


'''======================================'''

'''ITERATIVE DEPTH FIRST TRAVERSAL'''

def depthFirst(root):
    if root == None:
        result = []
        return result
    
    stack = [ root ]
    while len(stack) > 0:
        currentNode = stack.pop()

        if (currentNode.left): 
            stack.append(currentNode.left)
        if (currentNode.right): 
            stack.append(currentNode.right)

print(depthFirst(root))
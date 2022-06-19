class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
def insert(node, data):
    if node is None :
        return Node(data)
    else:
        if data <= node.data:
            node.left = insert(node.left, data)
        else:
            node.right = insert(node.right, data)
        return node
 
def minValue(node):
    if node.left == None:
        return node.data
    return minValue(node.left)
 
if __name__ == "__main__" :
    root = None
    root = insert(root, 4)
    insert(root, 2)
    insert(root, 1)
    insert(root, 3)
    insert(root, 6)
    insert(root, 5)
    print(minValue(root))
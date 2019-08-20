class MyBinaryNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right
    
    def __str__(self):
        return str(self.val)
    
    def __repr__(self):
        return str(self)


class MyBinaryTree(object):
    def __init__(self, head=None):
        self.head = head
    
    def insert(self, val, head, parent=None):
        pass

    def delete(self, val):
        p_delete(val, self.head, None)

    def p_delete(self, val, node=None, parent=None):
        if node is None:
            node = self.head
        if self.isEmpty():
            raise IndexError("Cannot delete from an empty binary tree.")
        elif node.val == val:
            if node.left and node.right:
                # Replace the deleted node with the value 
                if parent.left is node:
                    parent.left = getAndDeleteSmallestNode(node.right)
                else:
                    parent.right = getAndDeleteSmallestNode(node.right)
            elif node.left:
                if parent.left is node:
                    parent.left = node.left
                else:
                    parent.right = node.left
            elif node.right:
                if parent.left is node:
                    parent.left = node.right
                else:
                    parent.right = node.right
            else:
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
                return node
                
        elif val < node.val:
            return delete(self, val, node.left, node)
        else:
            return delete(self, val, node.right, node)
    
    def getAndDeleteSmallestNode(self, tree):
        pass
         
    
    def search(self, head, val):
        if head is None:
            return False
        elif head.val == val:
            return True
        elif val < head.val:
            return search(self, head.left, val)
        else:
            return search(self, head.right, val)
    
    def traverse(self):
        pass

    def isEmpty(self):
        return len(self) == 0

    def _len__(self):
        pass

    def str(self):
        pass

    def repr(self):
        pass

class MyBinarySearchTree(object):
    pass


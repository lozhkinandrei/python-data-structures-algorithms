
class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = None
        self.right = None

    def insert_left(self, key):
        if self.left:
            temp = Node(key)
            temp.left = self.left
            self.left = temp
        else:
            self.left = Node(key)

    def insert_right(self, key):
        if self.right:
            temp = Node(key)
            temp.right = self.right
            self.right = temp
        else:
            self.right = Node(key)

    def preorder(self):
        result = []

        result.append(self.key)

        if self.left:
            result += self.left.preorder()
        if self.right:
            result += self.right.preorder()

        return result

    def postorder(self):
        result = []

        if self.left:
            result += self.left.postorder()
        if self.right:
            result += self.right.postorder()

        result.append(self.key)
        return result

    def inorder(self):
        result = []

        if self.left:
            result += self.left.inorder()

        result.append(self.key)

        if self.right:
            result += self.right.inorder()

        return result

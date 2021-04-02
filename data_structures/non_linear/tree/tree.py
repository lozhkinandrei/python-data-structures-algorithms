from queue import Queue


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

    def breadth_first_traversal(self):
        result = []

        queue = Queue()
        queue.put(self)

        while queue.qsize() > 0:
            node = queue.get()
            result.append(node.key)

            if node.left:
                queue.put(node.left)

            if node.right:
                queue.put(node.right)

        return result

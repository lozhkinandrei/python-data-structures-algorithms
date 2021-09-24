class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def add(self, value):
        self.head = Node(value, self.head)
        self._size += 1

    def append(self, value):
        node = self.head

        if node:
            while node.next:
                prev = node
                node = node.next
            node.next = Node(value)
        else:
            self.head = Node(value)

        self._size += 1

    def search(self, value):
        node = self.head
        while node:
            if node.value == value:
                return True
            node = node.next
        return False

    def remove(self, value):
        if self.index(value):
            node = self.head
            while node:
                if node.value == value:
                    prev.next = node.next
                    self._size -= 1
                    break
                prev = node
                node = node.next

    def index(self, value):
        node = self.head
        index = 0
        while node:
            if node.value == value:
                return index
            index += 1
            node = node.next
        raise ValueError("{} is not in list".format(value))

    def pop(self, pos=None):
        node = self.head
        index = 0

        if node is None:
            raise IndexError("pop from empty list")

        if pos is not None:
            if pos == 0:
                self._size -= 1
                value = self.head.value
                self.head = self.head.next
                return value

            while node.next:
                prev = node
                node = node.next
                index += 1
                if index == pos:
                    self._size -= 1
                    prev.next = node.next
                    return node.value
            raise IndexError("pop index out of range")

        while node.next:
            prev = node
            node = node.next
        prev.next = None
        self._size -= 1
        return node.value

    def size(self):
        return self._size

    def is_empty(self):
        return self.head == None

    def __str__(self):
        items = []
        node = self.head

        while node:
            items.append(node.value)
            node = node.next

        return str(items)

    def __repr__(self):
        items = []
        node = self.head
        while node:
            items.append(node.value)
            node = node.next

        return f"Linked List: head -> {str(items)} <- tail"

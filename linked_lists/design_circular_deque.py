class LinkedListNode:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node


class MyCircularDeque:

    def __init__(self, k: int):
        self.max_size = k
        self.current_size = 0
        self.front = None
        self.back = None

    def insertFront(self, value: int) -> bool:
        if not self.front:
            self.front = LinkedListNode(value)
            self.back = self.front
            self.current_size = 1
            return True

        if self.current_size >= self.max_size:
            return False

        new_node = LinkedListNode(value, self.front, None)
        self.front.prev = new_node
        self.current_size += 1
        self.front = new_node
        return True

    def insertLast(self, value: int) -> bool:
        if not self.front:
            self.front = LinkedListNode(value)
            self.back = self.front
            self.current_size = 1
            return True

        if self.current_size >= self.max_size:
            return False

        new_node = LinkedListNode(value, None, self.back)
        self.back.next = new_node
        self.current_size += 1
        self.back = new_node
        return True

    def deleteFront(self) -> bool:
        if not self.front:
            return False

        if self.back == self.front:
            self.back = None
            self.front = None
            self.current_size -= 1
            return True

        self.front = self.front.next
        self.current_size -= 1
        return True

    def deleteLast(self) -> bool:
        if not self.front:
            return False

        if self.back == self.front:
            self.back = None
            self.front = None
            self.current_size -= 1
            return True

        self.back = self.back.prev
        self.current_size -= 1
        return True

    def getFront(self) -> int:
        if not self.front:
            return -1

        return self.front.value

    def getRear(self) -> int:
        if not self.front:
            return -1
        print(self.front.value)
        return self.back.value

    def isEmpty(self) -> bool:
        return not self.front

    def isFull(self) -> bool:
        return self.current_size == self.max_size

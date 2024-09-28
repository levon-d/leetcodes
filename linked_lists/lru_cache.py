class LinkedListNode:
    def __init__(self, key, value, next_node=None, prev=None):
        self.key = key
        self.value = value
        self.next = next_node
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.elems = {}
        self.capacity = capacity
        self.current_size = 0
        self.most_recent, self.least_recent = LinkedListNode(-1,-1), LinkedListNode(-1,-1)
        self.least_recent.next = self.most_recent
        self.most_recent.prev = self.least_recent

    def remove(self, node):
        prev, nxt = node.prev, node.next 
        prev.next = nxt 
        nxt.prev = prev


    def insert(self, node):
        prev, nxt = self.most_recent.prev, self.most_recent

        node.prev = prev 
        node.next = nxt

        nxt.prev = node

        prev.next = node 
        

    def get(self, key: int) -> int:
        if key not in self.elems:
            return -1

        self.remove(self.elems[key])
        self.insert(self.elems[key])

        return self.elems[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.elems:
            self.remove(self.elems[key])
            self.elems[key].value = value
            self.insert(self.elems[key])
            return

        self.elems[key] = LinkedListNode(key, value)
        self.insert(self.elems[key])
        self.current_size += 1 

        if self.current_size > self.capacity:

            del self.elems[self.least_recent.next.key]
            self.remove(self.least_recent.next)

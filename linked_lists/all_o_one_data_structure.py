class LinkedListNode:
    def __init__(self, key, count):
        self.key = key
        self.count = count
        self.next = None
        self.prev = None


class AllOne:

    def __init__(self):
        self.max = LinkedListNode(0, float("inf"))
        self.min = LinkedListNode(0, float("-inf"))
        self.min.next = self.max
        self.max.prev = self.min
        self.nodes = {}

    def inc(self, key: str) -> None:
        if key not in self.nodes:
            new_node = LinkedListNode(key, 1)
            self.min.next.prev = new_node
            new_node.next = self.min.next
            new_node.prev = self.min
            self.min.next = new_node
            self.nodes[key] = new_node
            return

        node = self.nodes[key]
        node.count += 1
        
        while node.count > node.next.count:
            next_node, prev_node = node.next, node.prev

            prev_node.next = next_node
            next_node.prev = prev_node

            node.next = next_node.next
            node.prev = next_node
            next_node.next.prev = node
            next_node.next = node 

            

    def dec(self, key: str) -> None:
        node = self.nodes[key]
        if node.count == 1:
            node.prev.next = node.next
            node.next.prev = node.prev
            del self.nodes[key]
            return

        node.count -= 1

        while node.count < node.prev.count:
            prev_node, next_node = node.prev, node.next

            prev_node.next = next_node
            next_node.prev = prev_node

            node.prev = prev_node.prev
            node.next = prev_node
            prev_node.prev.next = node
            prev_node.prev = node


    def getMaxKey(self) -> str:
        if self.max.prev == self.min:
            return ""
        return self.max.prev.key

    def getMinKey(self) -> str:
        if self.min.next == self.max:
            return ""
        return self.min.next.key



# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

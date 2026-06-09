class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_tail(self, node):
        node.prev = self.tail.prev
        node.next = self.tail

        self.tail.prev.next = node
        self.tail.prev = node

    def remove_head(self):
        node = self.head.next
        self.remove_node(node)
        return node

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev = None
        node.next = None

    def move_to_tail(self, node):
        self.remove_node(node)
        self.add_to_tail(node)

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity

        self.item_dict = {}
        self.linked_list = LinkedList()

    def get(self, key: int) -> int:
        node = self.item_dict.get(key)

        if not node:
            return -1

        self.linked_list.move_to_tail(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.item_dict.get(key)

        if node:
            node.value = value
            self.linked_list.move_to_tail(node)
        else:
            node = Node(key, value)
            self.item_dict[key] = node
            self.linked_list.add_to_tail(node)

            if len(self.item_dict) > self.capacity:
                del_node =  self.linked_list.remove_head()

                del self.item_dict[del_node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

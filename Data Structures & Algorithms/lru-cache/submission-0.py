class Node:
    def __init__(self, key=0, val=0):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.LRU={}
        self.head=Node()
        self.tail=Node()
        self.head.next=self.tail
        self.tail.prev=self.head

    def _remove(self,node):
        nxt=node.next
        prv=node.prev
        nxt.prev=prv
        prv.next=nxt

    def _add(self, node):
        node.prev=self.head
        node.next=self.head.next
        node.next.prev=node
        node.prev.next=node

    def get(self, key: int) -> int:
        if key in self.LRU:
            node=self.LRU[key]
            # move to front of list
            self._remove(node)
            self._add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.LRU:
            # move to front of list
            self._remove(self.LRU[key])

        new_node=Node(key,value)
        self.LRU[key]=new_node
        self._add(new_node)

        if len(self.LRU)>self.capacity:
            last=self.tail.prev
            self._remove(last)
            del self.LRU[last.key]


class Node:
    def __init__(self, val, key=-1, next=None, prev=None):
        self.val=val
        self.key=key
        self.next=next
        self.prev=prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cache=dict()
        self.head=Node(val=float('inf'))
        self.tail=Node(val=float('inf'))
        self.head.next=self.tail
        self.tail.prev=self.head
        self.capacity=capacity
        self.count=0

    def get(self, key: int) -> int:
        if key in self.cache:
            node=self.cache[key]
            node.prev.next=node.next
            node.next.prev=node.prev
            node.prev=self.tail.prev
            node.next=self.tail
            self.tail.prev.next=node
            self.tail.prev=node
            print(node.val, self.tail.prev.val)
            return node.val
        else:
            return -1

        

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key not in self.cache:
            if self.count<self.capacity:
                print(self.head.next.val)
                self.count+=1
                node=Node(key=key, val=value, next=self.tail, prev=self.tail.prev)
                self.tail.prev.next=node
                self.tail.prev=node
                self.cache[key]=node
            else:
                toberemoved=self.head.next
                toberemoved.next.prev=self.head
                self.head.next=toberemoved.next
                del self.cache[toberemoved.key]

                node=Node(key=key,val=value,prev=self.tail.prev,next=self.tail)
                self.tail.prev.next=node
                self.tail.prev=node
                self.cache[key]=node
        else:
            node=self.cache[key]
            node.prev.next=node.next
            node.next.prev=node.prev
            node.val=value
            node.prev=self.tail.prev
            node.next=self.tail
            self.tail.prev.next=node
            self.tail.prev=node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
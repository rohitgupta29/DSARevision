
"""
Psudo code:

1. Add:

Map contains Key:

    if contain, get the address
    9:35 AM (update it)



Delete:

1. Remove the tail
2. Remove from Hash Map

Get:

1. If Hashmap contains key:
    get address of the node from Hashmap
    remove the node
    add to the front
  else:
    return -1

"""


class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self,capacity):

        self.cap = capacity
        self.cache = {}
        #set values for head and tail
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        # to implement doubly linked list
        self.head.next = self.tail
        self.tail.prev = self.head
        ## rest of nodes will be added in between head and tail
        # inserting of element will be after head in the linked list

    def get(self,key):
        # Does the key exist in the hashmap
        if key in self.cache:
            node = self.cache[key]
            # delete it and insert it rifht after head
            self.moveTofront(node)
            return node.value
        return -1

    def put(self, key,value) -> None:

        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.moveToFront(node)
            return node.value
        node = Node(key,value)
        if self.size < self.cap:
            self.insertAtHead(node)
            self.size +=1
        else:
            self.deleteLastNode()
            self.insertAtHead(node)
        self.cache[key] = node
        return value

    def moveToFront(self, node: Node):
        self.deleteNode(node)
        self.insertAtHead(node)


    def deleteNode(self, node:Node):
        node.next.prev = node.prev
        node.prev.next = node.next


    def insertAtHead(self, node:Node):
        # next of node will replace the next of head
        node.next =self.head.next
        # prev of node will connect to dummy head we had created
        node.prev = self.head
        #prev of next element of head will be node now
        self.head.next.prev = node
        # next of the dummy head is node
        self.head.next = node

    def deleteLastNode(self):
        #define the last node
        node = self.tail.prev
        # get the key of node from the cache
        del self.cache[node.key]
        #delete the node
        self.deleteNode(node)


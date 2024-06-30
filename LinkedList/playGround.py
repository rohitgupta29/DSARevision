



class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtIndex(self, data, index):

        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(data)
        else:
            while(current_node != None and position + 1 != index):
                position = position + 1
                current_node = current_node.next

            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")

    def insertAtEnd(self, data):

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while(current_node.next):
            current_node= current_node.next

        current_node.next = new_node

    ## Deleting the node

    def remove_first_node(self):

        if (self.head == None):
            return
        if (self.head.next == None):
            self.head = self.head.next

    def remove_at_index(self, index):

        if self.head == None:
            return

        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while (current_node != None and position + 1 != index):
                position = position + 1
                current_node = current_node.next

            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("index is not present in the LL")

    def delete_last_node(self):

        if self.head is None:
            return
        current_node  = self.head

        while(current_node.next.next):
            current_node = current_node.next

        current_node.next = None

        pass


    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next




if __name__ == '__main__':
    # create a new linked list
    llist = LinkedList()

    # add nodes to the linked list
    llist.insertAtEnd('a')
    llist.insertAtEnd('b')
    llist.insertAtBegin('c')
    llist.insertAtEnd('d')
    llist.insertAtIndex('g', 2)

    # print the linked list
    print("Node Data")
    llist.printLL()


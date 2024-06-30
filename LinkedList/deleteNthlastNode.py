

class Node:

    def __init__(self,data):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def remove(self, index):
        if self.head == None:
            return

        current = self.head
        position = 0

        if position == index:
            self.head = self.head.next
        else:

            while current != None and position != index:
                position = position +1
                current = current.next

                if current.next != None:
                    current = current.next






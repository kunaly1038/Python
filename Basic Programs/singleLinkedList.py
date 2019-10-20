class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = newNode

    def printList(self):
        if self.head is None:
            print('List is Empty')
        else:
            cur = self.head
            while cur is not None:
                print(cur.data)
                cur = cur.next


x = List()
x.printList()
x.insert(2)
x.insert(4)
x.insert(45)
x.insert(43)
x.printList()

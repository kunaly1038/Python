class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None

    def insertAtBegin(self):
        data = input('Enter the Data : ')
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            # newNode.next = self.head
            # self.head = newNode
            temp = self.head
            self.head = newNode
            self.head.next = temp

    def insertAtEnd(self):
        data = input('Enter the Data : ')
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            start = self.head
            while start.next is not None:
                start =  start.next
            start.next = newNode

    def deleteAtBegin(self):
        if self.head is None:
            print('List is empty')
        else:
            self.head = self.head.next

    def deleteAtEnd(self):
        if self.head is None:
            print('List is empty')
        else:
            start = self.head
            temp = self.head
            while start.next is not None:
                temp = start
                start = start.next
            temp.next = None


    def printList(self):
        if self.head is None:
            print('List is empty')
        else:
            start = self.head
            while start is not None:
                print(start.data)
                start = start.next


if __name__ == '__main__':
    import sys
    single = List()
    while True:
        user = input('To continue Press Y : ')
        if user is 'y' or user is 'Y':
            print('1 : Insert At Begin',)
            print('2 : Insert At End')
            print('3 : Delete At Begin')
            print('4 : Delete At End')
            print('5 : Insert At Position')
            print('6 : Delete At Position')
            print('7 : Length of the List')
            print('8 : Print the List')
            userInput = input('Enter You choice :')
            if userInput is '1':
                single.insertAtBegin()
                single.printList()
            elif userInput is '2':
                single.insertAtEnd()
                single.printList()
            elif userInput is '3':
                single.deleteAtBegin()
                single.printList()
            elif userInput is '4':
                single.deleteAtEnd()
                single.printList()
            elif userInput is '8':
                single.printList()

        else:
            sys.exit()

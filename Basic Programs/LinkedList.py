class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertBegin(self):
        Data = input('Enter the Data : ')
        new = Node(Data)
        if self.head is None:
            self.head = new
        else:
            start = self.head
            self.head = new
            self.head.next = start

    def insertAtEnd(self):
        Data = input('Enter the Data : ')
        new = Node(Data)
        if self.head is None:
            self.head = new
        else:
            start = self.head
            while start.next is not None:
                start = start.next
            start.next = new

    def insertAtPostion(self, count):
        print('Enter Position between 0 to ', count)
        post = input('Enter the Position : ')
        if self.head is None:
            print('List is empty')
        elif int(count) > int(post):
            Data = input('Enter the Data : ')
            new = Node(Data)
            start = self.head
            start2 = Node()
            flag = 0
            for flag in range(1, int(post)):
                start2 = start
                start = start.next
                flag +=1
            start2.next = new
            new.next = start

    def deleteAtBegin(self):
        if self.head is None:
            print('List is Empty')
        else:
            self.head = self.head.next

    def deleteAtEnd(self):
        if self.head is None:
            print('List is Empty')
        else:
            start = self.head
            start2 = self.head
            while start.next is not None:
                start2 =start
                start = start.next
            start2.next = None


    def deleteAtPosition(self, count):
        print('Enter Position between 0 to ', count)
        post = input('Enter the Position : ')
        if self.head is None:
            print('List is empty')
        elif int(count) > int(post):
            start = self.head
            start2 = self.head
            flag = 0
            for flag in range(1, int(post)):
                start2 = start
                start = start.next
                flag +=1
            start2.next = start.next

    def printList(self):
         if self.head is None:
            print('List is Empty')
         else:
             start = self.head
             while start is not None:
                 print(start.data)
                 start = start.next


    def listCount(self):
        count = 0
        if self.head is None:
            print('List is Empty')
        else:
            start = self.head
            while start is not None:
                start = start.next
                count += 1
        return count



if __name__ == '__main__':
    import sys
    list = LinkedList()
    while True:
        desc = input('Press Y to continue : ')
        if desc is 'y' or desc is 'Y':
            print('1. Insert At Begin.')
            print('2. Insert At End.')
            print('3. Insert At Position.')
            print('4. Delete At Begin.')
            print('5. Delete At End.')
            print('6. Delete At Position.')
            print('7. Print the List.')
            print('8. Get List Count.')
            choice = input('Enter Your Choice : ')
            if choice is '1':
                list.insertBegin()
                list.printList()
                print('===================================')
            elif choice is '2':
                list.insertAtEnd()
                list.printList()
                print('===================================')
            elif choice is '3':
                count = list.listCount()
                list.insertAtPostion(count)
                list.printList()
                print('===================================')
            elif choice is '4':
                list.deleteAtBegin()
                list.printList()
                print('===================================')
            elif choice is '5':
                list.deleteAtEnd()
                list.printList()
                print('===================================')
            elif choice is '6':
                count = list.listCount()
                list.deleteAtPosition(count)
                list.printList()
                print('===================================')
            elif choice is '7':
                list.printList()
                print('===================================')
            elif choice is '8':
                count = list.listCount()
                print(count, ' number of nodes in List')

        else:
            sys.exit()

# Binary Tree insertion and print the nodes into the binary tree

class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insertBinaryTree(self,data):
        if self.data:
            if self.data > data:
                if self.left is None:
                    self.left =  node(data)
                else:
                    self.left.insertBinaryTree(data)
            elif self.data < data:
                if self.right is None:
                    self.right =  node(data)
                else:
                    self.right.insertBinaryTree(data)
            else:
                self.data = data

                
    def printBinaryTree(self):
        if self.left:
            self.left.printBinaryTree()
        print(self.data)
        if self.right:
            self.right.printBinaryTree()



insertRoot = int(input('Enter the root node value :'))
root = node(insertRoot)
while True:
    continueUser = str(input('Enter y if you want to enter the values :'))
    if continueUser is 'y':
        userInput = int(input('Enter the child values into the Binary Tree :'))
        root.insertBinaryTree(userInput)
    else:
        break
    

root.printBinaryTree()

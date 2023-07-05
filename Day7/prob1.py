### Insert a node at the begining of the linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
    
    def begining_insert(self,new_data):

        ##creating a new node
         new_node = Node(new_data)
        ## inserting at the begining
         new_node.next = self.head
         self.head = new_node

    ## print the linked list
    def printList(self):
        temp = self.head
        while temp:
            print(str(temp.data)+" ",end=" ")
            temp = temp.next


llist = linkedList()
llist.begining_insert(1)
llist.begining_insert(5)
llist.begining_insert(4)
llist.begining_insert(3)
llist.begining_insert(2)
llist.printList()
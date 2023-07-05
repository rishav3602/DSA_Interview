### Insert at the end of the linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def endInsert(self,new_data):

        ## creating a new node
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        
        ## inserting at the end 
        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = new_node


    def printList(self):
        temp = self.head
        while temp:
            print(str(temp.data)+" ",end="")
            temp = temp.next

llist = linked_list()
llist.endInsert(1)
llist.endInsert(2)
llist.endInsert(3)
llist.endInsert(4)
llist.endInsert(5)
llist.endInsert(6)
llist.printList()
        

## insert after any given node:

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:

    def __init__(self):
        self.head = None

    def endInsert(self, new_data):
        ## creating a new node 
        new_node = Node(new_data)

        ##inserting at end
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node


    def anywhereInsert(self, prev, new_data):
        if prev is None:
            print("the previous node should must present in the node")
            return
        
        new_node = Node(new_data)
        new_node.next = prev.next
        prev.next = new_node


    def printList(self):
        temp = self.head
        while temp:
            print(str(temp.data)+" ",end="")
            temp = temp.next

llist = linkedList()
llist.endInsert(1)
llist.endInsert(2)
llist.endInsert(3)
llist.endInsert(4)
llist.endInsert(5)
llist.endInsert(6)
llist.anywhereInsert(llist.head.next.next.next,76)
llist.printList()

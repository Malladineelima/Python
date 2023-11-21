class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CreateList:
    def __init__(self):
        self.head=Node(None)
        self.tail=Node(None)
        self.head.next=self.tail
        self.tail.next=self.head
    #adding node at end of LL
    def add(self,data):
        newNode=Node(data)
        #is empty?
        if self.head.data is None:#is empty
            self.head=newNode
            self.tail=newNode
            newNode.next=self.head
        else:
            self.tail.next=newNode
            self.tail=newNode 
            #it is CLL so,tail will point to head
            self.tail.next=self.head
        def display(self):
            current=self.head
            if self.head is None:
                print("list is empty")
                return
            else:
                print("Nodes of the circular linked list:")
                print(current.data,"-->")
                while(current.next!=self.head):
                    current=current.next
                    print(current.data,"-->")
class Circularlinkedlist:
    cl=CreateList()
    cl.add("S")
    cl.add("M")
    cl.add("I")
    cl.add("L")
    cl.add("E")
    cl.display()

    


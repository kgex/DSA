class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
 
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
   
    def insertFirst(self,value):
        node = Node(value)
        node.next = self.head
        self.head = node
        if (self.tail == None):
            self.tail = self.head
        self.size += 1
 
    def head_LL(self):
        return self.head.data
   
    def tail_LL(self):
        return self.tail.data
 
    def display(self):
        temp = self.head
        while(temp != None):
            print(temp.data , "--->" , end = " ")
            temp = temp.next
        print("END")
 
    def insertLast(self,value):
        node = Node(value)
        self.tail.next = node
        self.tail = node
        self.size += 1
 
 
    def insertAtIndex(self,index,value):
        if(index == 0):
            return self.insertFirst()
        if(index == self.size - 1):
            return self.insertLast()
 
        node = Node(value)
 
        temp = self.head
 
        for i in range(1,index - 1):
            temp = temp.next
       
        node.next = temp.next
        temp.next = node
        self.size += 1
 
    def search(self,value):
        temp = self.head
        count = 0
        while(temp != None):
            if (temp.data == value):
                print("found at ", count )
                return temp.data
            temp = temp.next
            count += 1
        return -1
 
    def deleteFirst(self):
        self.head = self.head.next
        self.size -= 1
 
    def deleteAtLast(self):
 
        temp = self.head
        for i in range(self.size-2):
            temp = temp.next
        print(temp.data)
        temp.next = None
 
    def deleteAtIndex(self,index):
 
        temp = self.head
 
        for i in range(index-1):
            temp = temp.next
 
        temp.next = temp.next.next
 
   
 
if __name__ == '__main__':
    LL = LinkedList()
    LL.insertFirst(2)
    LL.insertFirst(4)
    LL.insertFirst(5)
    LL.insertFirst(6)
    LL.insertFirst(7)
    LL.display()
 
    LL.insertLast(77)
    LL.insertLast(55)
 
    LL.deleteFirst()
    LL.display()
    LL.deleteAtLast()
    LL.display()
    LL.deleteAtIndex(2)
    LL.display()


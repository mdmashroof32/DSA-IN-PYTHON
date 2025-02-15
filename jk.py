
class Node:
    def __init__(self,item = None,next = None):
        self.item =item
        self.next =next

class List:
    def __init__(self,start = None):
        self.start =start
    def empty(self):
        return self.start == None

    def insertfirst(self,data):
        n = Node(data,self.start)
        self.start = n

    def insertlast(self,data):
        n = Node(data)
        if not self.empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.start = n
    def search(self,data):
        temp = self.start
        while temp is not None:
            if temp.item ==data:
                return temp
            temp = temp.next
        return  None

    def insertafter(self,temp,data=None):
        if temp is not None:
            n = Node(data,temp.next)
            temp.next =n
    def printlist(self):
        temp =self.start
        while temp is not  None:
            print(temp.item,end= " ")
            temp = temp.next
    def  deletfirst(self):
        if self.start is not None:
            self.start =self.start.next

    def deletelast(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
    def deleteitem(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item ==data:
                self.start = None
        else:
            temp = self.start

            if temp.item ==data:
                self.start = temp.next
            else:
               while temp.next is not None:
                   if temp.next.item ==data:
                       temp.next =temp.next.next
                       break
                   temp =temp.next
    def __iter__(self):
        return iterator(self.start)
class iterator:
    def __init__(self,start):
        self.current = start
    def __itre__(self):
         return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data =self.current.item
        self.current =self.current.next




m =List()
m.insertfirst(78)
m.insertlast(45)
m.insertlast(99)
m.insertafter(m.search(45),800)
m.deletfirst()
m.printlist()
m.deleteitem(800)
m.deletelast()
for i in m:
    print( i , end = " ")

class Node:
    def __init__(self,prev =None,item = None, next = None):
        self.prev =prev
        self.item = item
        self.next =next

class Dll:
    def __init__ (self,start =None):
        self.start = start

    def empty(self):
        return self.start == None

    def insertfirst(self,data):
        n =Node(item =data,next = self.start)
        if not  self.empty():
             self.start.prev = n
        self.start = n
    def insertlast(self,data):
        temp =self.start
        if temp is not None:
            while temp.next is not None:
                temp =temp.next

        n = Node(temp,data,None)
        if temp==None:
            self.start = n
        else:
            temp.next = n
    def search(self,data):
        temp =self.start
        while temp != None:
            if temp.item ==data:
                return temp
            temp = temp.next
        return None
    def insertafter(self,temp,data):
        if temp is not None:
            n = Node(temp,data,temp.next)
            if temp.next is not None:

                temp.next.prev =n
            temp.next =n

    def print(self):
        temp  =self.start
        while temp is not None:
            print(temp.item,end = " ")
        temp =temp.next

    def deletefirst(self):
        if self.start is not None:
            self.start =self.start.next
            if self.start is not None:
                self.start.prev = None


    def deletelast(self):
        if self.start is None:
            pass

        elif self.start.next is None:
            self.start =None

        else:
            temp = self.start
            while temp.next is not None:
               temp = temp.next
            temp.prev.next

    def deleteitem(self,data):
        if self.start is None:
            pass

        else :
            temp = self.start

            while temp is not None:
                if temp.item == data:
                  if temp.next is not  None:
                       temp.next.prev = temp.prev
                  if temp.prev is not None:
                      temp.prev.next = temp.next
                  else:
                     self.start = temp.next
                temp =temp.next

    def __iter__(self):
        return iterator(self.start)

class iterator:
    def __init__(self,start):
        self.current =start
    def __iter__(self):
        return  self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return  data

m1 = Dll()
m1.insertfirst(56)
m1.insertlast(55)
m1.insertafter(m1.search(55),44)
m1.deletefirst()
m1.deletelast()
m1.deleteitem(56)
for i in m1:
    print(i,end = " ")
print()



class Node:
    def __init__(self,item= None, next = None):
        self.item = item
        self.next = next

class Cll:
    def __init__(self,last=None):
        self.last = last

    def empty(self):
        return self.last == None

    def insertfist(self,data):
        n = Node(data)
        if  self.empty():
            self.last = n
            n.next =self.last
        else:
            n.next = self.last.next
            self.last.next = n

    def insertlast(self,data):
        n = Node(data)
        if self.empty():
            self.last = n
            n.next = self.last
        else:
            n.next= self.last.next
            self.last.next = n
            self.last = n

    def search(self,data):
        if self.empty():
            return None
        temp = self.last.next
        while temp is not self.last:
           if temp.item == data:
               return temp
           temp = temp.next
        if temp.item ==data:#check the last Node of the list
          return temp
        return None

    def insertafter(self,temp,data):
        if temp is not None:
            n = Node(data,temp.next)
            temp.next = n
            if temp==self.last:
                self.last = n

    def deletefirst(self):
        if self.last is None:
           pass
        elif self.last is self.last.next:
           self.last = None
        else:
           self.last.next =self.last.next.next

    def deletelast(self):
        if not self.empty():
            if self.last is self.last.next:
                self.last = None
            else:
                temp = self.last.next
                while temp.next is not self.last:
                    temp= temp.next
                temp.next = self.last.next
                self.last = temp

    def deleteitem(self,data):
        if not self.empty():
            if self.last is self.last.next:
                if self.last.item == data:
                  self.last = None
            else:
                if self.last.next.item ==data:
                    self.deletefirst()
                elif self.last.item == data:
                    self.deletelast()
                else:
                    temp = self.last.next
                    while temp is not self.last:
                       if temp.next.item == data:
                           temp.next = temp.next.next
                           break
                       temp = temp.next









    def __iter__(self):
        if self.last == None:
             return Iterator(None)
        else:
            return Iterator(self.last.next )
class Iterator:
    def __init__(self,start):
       self.current = start
       self.start =start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current == None:
            raise StopIteration

        data = self.current.item
        self.current = self.current.next
        if self.current == self.start:
            raise StopIteration
        return data




c = Cll()
c.insertfist(89)
c.insertfist(65)
c.insertlast(99)
c.insertlast(55)
#c.insertafter(c.search(89),90)
#c.deletefirst()
#c.deletelast()
c.deleteitem(55)


for i in c:
  print(i,end=" ")


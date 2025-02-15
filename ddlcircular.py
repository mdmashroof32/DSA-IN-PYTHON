
class Node:
    def __init__(self,prev =None,item =None,next= None):
        self.prev =prev
        self.item = item
        self.next = next

class DLCU:
    def __init__(self,start= None):
        self.start = start

    def empty(self):
        return self.start==None

    def insertfirst(self,data):
      n= Node(item=data)
      if self.empty():
         n.prev =n
         n.next =n
         self.start=n

      else:
          n.prev =self.start.prev
          n.next=self.start
          self.start.prev.next =n
          self.start.prev = n
          self.start = n

    def insertlast(self,data):
        n  = Node(item=data)
        if self.empty():
            n.prev = n
            n.next = n
            self.start = n

        else:
            n.prev = self.start.prev
            n.next = self.start
            n.prev.next = n
            self.start.prev = n

    def search(self,data):
        temp =self.start
        if temp == None:
            return  None
        if temp.item == data:
            return temp
        else:
         temp = temp.next
         while temp is not self.start :
            if temp.item == data:
                return temp
            temp = temp.next
         return None

    def insertafter(self,temp,data):

        if temp is not None:
            n= Node(temp,data,temp.next)
            temp.next.prev = n
            temp.next = n

    def printlist(self):
        temp = self.start
        if temp is not None:
            print(temp.item, end=" ")
            temp = temp.next
            while temp is not self.start:
                print(temp.item, end=" ")
                temp = temp.next

    def deletfirst(self):
        if not self.empty():
            if self.start.next ==self.start:
                self.start = None
            else:
             self.start.prev.next = self.start.next
             self.start.next.prev =self.start.prev
             self.start = self.start.next

    def deletelast(self):
        if not self.empty():
            if self.start.next ==self.start:
               self.start = None
            else:
                self.start.prev.prev.next = self.start
                self.start.prev =self.start.prev.prev

    def deleteitem(self,data,temp):
        if not self.empty():
         temp =self.start
         if temp.item == data:
            self.deletfirst()
         else:
             temp = temp.next
             while temp != self.start:
               if temp.item == data:
                 temp.prev.next =temp.next
                 temp.next,perv = temp.prev
               temp = temp.next
             return None

    def __iter__(self):
        return DLIterator(self.start)



class DLIterator:
    def __init__(self,start):
        self.current = start
        self.start =start
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        if self.current==self.start and self.count==1:
            raise StopIteration
        else:
            self.count = 1
        data = self.current.item
        self.current =self.current.next
        return data



s = DLCU()

s.insertfirst(90)
s.insertlast(86)
s.insertafter(s.search(90),54)
s.deletfirst()
s.deletelast()
for x in s:
    print(x,end=" ")
print()
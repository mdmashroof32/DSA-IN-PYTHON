
class Node:
    def __init__(self,item=None,next=None):
        self.item= item
        self.next = next

class SLL:
    def __init__(self):
        self.start = None
        self.item_count = 0 #to store the number of element
    def empty(self):
        return self.start == None

    def push(self,data):
        n = Node(data,self.start)
        self.start = n
        self.item_count += 1

    def pop(self):
        if not self.empty():
            data =self.start.item
            self.start =self.start.next
            return data
            self.item_count -= 1
        else:
            raise IndexError("stack is empty")
    def peek(self):
       if not self.empty():
         return self.start.item
       else:
           raise self.empty()
    def size(self):
        return self.item_count





    def print(self):
        temp =self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp =temp.next


s1= SLL()
s1.push(90)
s1.push(78)
s1.push(89)

print("pop element", s1.pop())
print("peek element",s1.peek())
print("size of stack ", s1.size())
s1.print()

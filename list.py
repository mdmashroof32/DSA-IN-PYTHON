class Stack:
    def __init__(self):
        self.items =[]

    def empty(self):
        return len(self.items)== 0
    def push(self,data):
        self.items.append(data)
    def pop(self):
        if not self.empty():
          return self.items.pop()
        else:
            raise IndexError("Stack is empty")
    def peek(self):
       if not self.empty():
           return self.items[-1]
       else:
           raise IndexError("Stack is empty")

    def sizestack(self):
            return len(self.items)

s1 =Stack()
s1.push(89)
s1.push(49)
s1.push(94)
s1.push(90)
print("remove element",s1.pop())
print(s1.peek())

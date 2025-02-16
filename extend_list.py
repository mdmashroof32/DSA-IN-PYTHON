from numpy.matlib import empty


class Stack(list):
    def empty(self):
        return len(self)==0
    def push(self,data):
        self.append(data)
    def pop(self):
        if not self.empty():
            super().pop()
        else:
            raise IndexError("list is empty")
    def peek(self):
        if not self.empty():
            return self[-1]
        else:
            raise IndexError("list is empty")
    def size(self):
        return len(self)
    def insert(self, index, data):
        raise AttributeError("No insert Atributes insert in stack")

s1 =Stack()

s1.push(90)
s1.push(53)
s1.push(45)
s1.push(37)
s1.push(78)
print(s1.peek())
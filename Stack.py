from DynamicArray import DynamicArray

class Stack:
    def __init__(self,cap):
        self.array = DynamicArray(cap)
        self.top = -1

    def push(self,element):
        if self.array.n-1 == self.array.cap-1:
            raise Exception("Stack is full")
        self.array.pushback(element)
        self.top+=1

    def pop(self):
        if self.isEmpty():
            raise Exception
        self.array.popback()
        self.top-=1

    def top(self):
        return self.top

    def isEmpty(self):
        return self.top == -1

    def size(self):
        return self.array.n

    def Print(self):
        for  i in range(self.array.n-1,-1,-1):
            print(self.array[i])
        print()


stack = Stack(10)

stack.push(48)
stack.push(55)
stack.push(66)
stack.push(4)
stack.push(56)
stack.push(45)
stack.push(45)
stack.push(45)
stack.push(45)
stack.push(888)


stack.pop()
stack.Print()




class Queue:
    def __init__(self,cap):
        self.cap = cap
        self.front = 0
        self.rear = 0
        self.n = 0
        self.ls = [0]*self.cap
    def enqueue(self,value):
        if self.cap==self.n:
            print("Queue is full")
            return
        self.ls[self.rear] = value
        self.rear = (self.rear+1) % self.cap
        self.n+=1

    def dequeue(self):
        if self.isEmpty():
            print("You cannot dequeue an element")
            return
        data = self.ls[self.front]
        self.ls[self.front] = None
        self.front+=1
        self.n-=1
        return data

    def isEmpty(self):
        return self.n==0

    def peek(self):
        return self.ls[self.front]

    def size(self):
        return self.n

    def Print(self):
        for i in range(self.n):
            print(self.ls[(self.front+i) % self.cap])
        print()

q = Queue(10)

q.enqueue(15)
q.enqueue(20)
q.enqueue(16)
q.enqueue(48)
q.enqueue(48)
q.enqueue(48)
q.enqueue(48)
q.enqueue(48)
q.enqueue(48)
q.enqueue(48)
q.enqueue(48)
q.enqueue(48)
q.enqueue(48)
q.dequeue()
print(q.isEmpty())
print(q.size())
q.Print()
q2 = Queue(10)
q2.dequeue()
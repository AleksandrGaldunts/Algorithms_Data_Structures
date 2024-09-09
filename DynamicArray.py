import ctypes

class DynamicArray:
    def __init__(self,cap):
        self.cap = cap
        self.n = 0
        self.array = self.make_array(cap)

    def capacity(self):
        return self.cap

    def include(self,data):
        if self.cap == self.n:
            self.__resize(2 * self.cap)
        for i in range(self.n):
            if self.array[i] == data:
                return True
            return False

    def emplace(self,index,data):
        if not 0<=index<=self.n:
            raise IndexError
        if self.n == self.cap:
            self.__resize(self.cap * 2 )
        self.array[index] = data

    def __str__(self):
        return f"Our array is  {[self.array[i] for i in range(self.n)]}"

    def insert(self,index,data):
        if not 0<=index<=self.n:
            raise IndexError("index must be within this range")
        if self.n == self.cap:
            self.__resize(self.cap * 2 )
        for i in range(self.n-1,index-1,-1):
            self.array[i+1]= self.array[i]
        self.array[index] = data
        self.n+=1


    def __resize(self,newcap):
        B = self.make_array(newcap)

        for i in range(self.n):
            B[i] = self.array[i]
        self.array = B
        self.cap = newcap

    def pushback(self,data):
        if self.n == self.cap:
            self.__resize(self.cap*2)
        self.array[self.n] = data
        self.n+=1

    def popback(self):
        if self.n ==0:
            print("You can not pop an element from empty array")
            return
        if self.n == self.cap:
            self.__resize(self.cap * 2)
        self.array[self.n-1] = None
        self.n-=1

    def removeAt(self,index):
        if not 0<=index<= self.n:
            raise IndexError("index must be within the following range")

        for i in range(index,self.n-1):
            self.array[i]= self.array[i+1]
        self.array[self.n-1]=None
        self.n-=1


    def reserve(self,newcap):
        return self.__resize(newcap)

    def make_array(self,newcap):
        return (newcap * ctypes.py_object)()

    def clear(self):
        for i in range(self.n):
            self.array[i]=0
        self.n = 0

    def size(self):
        return self.n

    def isEmpty(self):
        return  self.n==0


    def __getitem__(self,index):
        if not 0<=index<=self.n:
            raise IndexError("something went wrong")
        return self.array[index]

    def __setitem__(self, index, newvalue):
        if self.n == self.cap:
            self.__resize(self.cap * 2)
        if not 0<=index<=self.n:
            raise IndexError("something went wrong")
        self.array[index] = newvalue

    def shrinktoFit(self):
        self.cap = self.n

    def assign(self,B):
        if self.n > B.cap:
            raise ValueError("B array is less than our array")
        for i in range(0,self.n):
            B.array[i] = self.array[i]
        B.n=self.n





array = DynamicArray(5)
array.pushback(8)
array.pushback(3)
array.pushback(5)
array.pushback(7)
array.removeAt(1)
print(array)

print(array.capacity())
print(array.include(5))
array.emplace(1,11)
print(array)
array.clear()
print(array)
array.reserve(10)
print(array.capacity())
print(array.isEmpty())

array.pushback(5)
array.pushback(10)
array.pushback(12)
array.pushback(88)
print(array)
array2 = DynamicArray(10)
array.assign(array2)
print(array2)
print(array2.capacity())
array2.shrinktoFit()
print(array2.capacity())
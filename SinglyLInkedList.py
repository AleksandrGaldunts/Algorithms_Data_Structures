class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def push_back(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        tmp = self.head
        while tmp.next is not None:
            tmp = tmp.next
        tmp.next = newNode
        newNode.next = None

    def push_front(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode


    def pop_front(self):
        if self.head is None:
            print("You cannot pop element")
            return
        else:
            tmp = self.head
            self.head = self.head.next
            tmp = None

    def pop_back(self):
        if self.head is None:
            print("you cannot pop an element")
            return
        tmp = self.head
        while tmp.next.next is not None:
            tmp = tmp.next
        tmp.next=None


    def insert_after(self,prevNode,data):
        newNode  = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            curr = self.head
            while curr.data != prevNode.data:
                curr = curr.next
            newNode.next = curr.next
            curr.next = newNode

    def erase_after(self,prevNode):
        if self.head is None:
            print("You cannot erase an element")
            return
        else:
            curr = self.head
            while curr.data != prevNode.data:
                curr = curr.next
            tmp = curr.next
            curr.next = curr.next.next
            tmp = None

    def clear(self):
        if self.head is None:
            print("List is empty")
            return
        else:
            self.head = None

    def isEmpty(self):
       return self.head is None

    def front(self):
        if self.head is None:
            print("List is empty")
            return
        else:
            return self.head.data

    def print_list(self):
        if self.head is None:
            print("None")
        else:
            tmp = self.head
            while tmp is not None:
                print(tmp.data,end = "->")
                tmp = tmp.next
                if tmp is None:
                    print("None")

    def reverse(self):
        if self.head is None:
            print("there is no element to reverse")
            return
        prev = None
        curr = self.head
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def merge(self,other):
        if self.head is None and other.head is not None:
            return other
        elif self.head is None and other.head is None:
            print("both lists are none")
            return
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = other.head

    def sort_list(self):
        pass


def merge_sorted_list(first,second):

    list3 = Node(-1)
    dummyNode = list3

    while first and second:
        if first.data<=second.data:
            dummyNode.next = first
            first = first.next
        else:
            dummyNode.next = second
            second = second.next

        dummyNode = dummyNode.next

    if first:
        dummyNode.next = first
    if second:
        dummyNode.next = second

    list3=list3.next

    return list3



ll = SinglyLinkedList()

ll.push_back(15)
ll.push_back(20)
ll.push_back(25)
ll.push_back(30)
ll.push_back(35)

ll.push_front(10)
ll.push_front(5)
ll.push_front(0)

ll.pop_back()
ll.pop_front()

ll.insert_after(Node(10),12.5)

#ll.clear()

print(ll.isEmpty())

print(ll.front())

ll.erase_after(Node(10))


ll.reverse()

list2 = SinglyLinkedList()
list2.push_back(999)
list2.push_back(99)
list2.push_back(9)

list2.print_list()

ll.merge(list2)

ll.print_list()


first = SinglyLinkedList()
first.push_back(10)
first.push_back(15)
first.push_back(20)

second = SinglyLinkedList()
second.push_back(11)
second.push_back(16)
second.push_back(21)

ls3=SinglyLinkedList()
ls3.head=merge_sorted_list(first.head,second.head)
ls3.print_list()


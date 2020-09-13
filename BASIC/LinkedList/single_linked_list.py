class Node:
    def __init__(self, val):
        self.val = val
        self.next=None
        

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.start = None

    def traverse(self, p=None):
        res=[]
        if p is None:
            p =self.start
        while p is not None:
            res.append(p.val)
            p=p.next
            # print(p.val)
        return res
        

    def get(self, index: int, p=None) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if p is None:
            p = self.start
        i=0
        while p is not None:
            if i == index:
                return p.val
            p=p.next
            i+=1

        return -1
        

    def addAtHead(self, val: int, p=None) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if p is None:
            p =self.start
        temp = Node(val)
        temp.next = self.start
        self.start = temp 
        

    def addAtTail(self, val: int, p=None) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if p is None:
            p =self.start

        #temp=Node(val)
        if self.start is None:
            self.addAtHead(val)
            return

        p=self.start
        while p.next is not None:
            p=p.next
        p.next=Node(val)


        
        

    def addAtIndex(self, index: int, val: int, p=None) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if p is None:
            p =self.start
        if index == 0:
            temp=Node(val)
            temp.next = self.start
            self.start = temp

        i=1
        while p is not None:
            if i == index:
                temp=Node(val)
                temp.next = p.next
                p.next = temp
                break
            p=p.next
            i+=1
        

    def deleteAtIndex(self, index: int, p=None) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if p is None:
            p =self.start
        if index == 0:            
            self.start = self.start.next

        i=1
        while p.next is not None:
            if i == index:
                p.next = p.next.next
                break
            p=p.next
            i+=1

    def cycle_creation(self, pos, p=None):
        if p is None:
            p =self.start
        i=0
        linker = None
        while p.next is not None:
            if pos == i:
                linker = p

            i+=1
            p=p.next
        if linker is not None:
            p.next=linker
            return True
        else:
            return False

    def cycle_detection(self, p=None):
        if p is None:
            p =self.start
        q=p
        while(p.next is not None and q.next is not None):
            p=p.next
            q=q.next
            if q.next is not None:
                q=q.next
            else:
                return False
            
            if p ==q:
                return p
        return False

    def cycle_remove(self):
        p = self.cycle_detection()
        if p == False:
            return "No cycle exist"
        q=p.next
        len_cycle=1
        while p != q:
            q=q.next
            len_cycle+=1
        # print("len_cycle:", len_cycle)
        
        s=self.start
        len_rem=0
        while (p != s):
            s=s.next
            p=p.next
            len_rem+=1
        
        total=len_rem+len_cycle
        print(total)
        s=self.start
        while total > 1:
            s=s.next
            total-=1

        s.next=None
        return s.val

    def reverse_iterative(self):
        p=self.start
        q=None
        r=None

        while(p is not None):
            r=q
            q=p
            p=p.next
            q.next=r
        self.start=q

        return True
        
    def split(self):
        slow=self.start
        fast=slow.next.next
        while fast is not None:
            slow=slow.next
            fast=fast.next
            if fast is not None:
                fast=fast.next

        second=slow.next
        slow.next=None
        first=self.start
        print(self.traverse())
        print(self.traverse(second))
        self.reverse_iterative()
        print(self.traverse())


    

        

        
     

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(2)
# obj.addAtHead(3)
# obj.addAtTail(0)
# obj.addAtTail(4)


# obj.addAtTail(3)
# obj.addAtTail(2)
# obj.addAtTail(0)
# obj.addAtTail(4)
# print("Cycle created: ",obj.cycle_creation(1))

obj.addAtTail(1)
obj.addAtTail(2)
obj.addAtTail(3)
obj.addAtTail(4)
obj.addAtTail(5)
# print("Cycle created: ",obj.cycle_creation(0))

# obj.addAtTail(1)
# obj.addAtTail(2)
# print("Cycle created: ",obj.cycle_creation(0))
# obj.addAtIndex(1, -1)
# obj.deleteAtIndex(2)``
# print("Traversal", obj.traverse())
# print("Cycle detection:", obj.cycle_detection())
# print("Cycle remove: ", obj.cycle_remove())
# print("Cycle detectoin:", obj.cycle_detection())
# print("Traversal", obj.traverse())
# print("Get value from index:", obj.get(2))
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)  

# obj.reverse_iterative()
print(obj.traverse())
print(obj.split())


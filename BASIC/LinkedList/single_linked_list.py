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
        # print(self.traverse())
        # print(self.traverse(second))
        self.reverse_iterative()
        # print(self.traverse())


    def merge(self, first, second):
        
        start=None
        if first is None and second is None:
            return None

        if first is None:
            return second
        
        if second is None:
            return first

        if first.val < second.val:
            start=first
            first=first.next
        else:
            start=second
            second=second.next

        p=start
        while first is not None and second is not None:
            if first.val < second.val:
                p.next=first
                first=first.next
            else:
                p.next=second
                second=second.next
            p=p.next

        while first is not None:
            p.next=first
            first=first.next
            p=p.next

        while second is not None:
            p.next=second
            second=second.next
            p=p.next

        print(self.traverse(start))
        return start

    def addTwoNumbers(self, l1, l2):

        carry=0
        start=Node(0)
        p=start

        if l1 is None or l2 is None:
            return l1 or l2
        while l1 is not None and l2 is not None:
            val =l1.val+l2.val+carry
            
            if val > 9:
                val=val-10
                carry=1
            else:
                carry=0
            p.next=Node(val)
            p=p.next
            l1=l1.next
            l2=l2.next

        while l1 is not None:
            val=l1.val+carry

            if val > 9:
                val=val-10
                carry=1
            else:
                carry=0
            p.next=Node(val)
            p=p.next
            l1=l1.next
        
        while l2 is not None:
            val=l2.val+carry

            if val >9:
                val=val-10
                carry=1
            else:
                carry=0
            p.next=Node(val)
            p=p.next
            l2=l2.next

        if carry ==1:
            p.next=Node(1)

        return start.next
            

    def bubble_sort(self):
        head=self.start
        flag=True
        i=head
        while i.next is not None:
            j=i.next
            while j is not None:
                print(obj.traverse())
                if i.val > j.val:
                    i.val, j.val = j.val, i.val
                j=j.next
            
            i=i.next
        return

    def merge_sort(self, head):
        if head is None or head.next is None:
            return head

        temp = head
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            temp=slow
            slow=slow.next
            fast=fast.next.next

        temp.next = None

        L= self.merge_sort(head)
        R = self.merge_sort(slow)
        print(self.traverse(L), self.traverse(R))
        return self.merge(L,R)



    

        

        
     

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
# param_1 = obj.get(index)
obj.addAtHead(-1)
obj.addAtTail(5)
obj.addAtTail(3)
obj.addAtTail(4)
obj.addAtTail(0)
# obj2.addAtTail(5)
# obj2.addAtTail(9)
print(obj.traverse())
#obj.bubble_sort()
obj.merge_sort(obj.start)
print(obj.traverse())

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
# print(obj.traverse())
# # print(obj.split())
# print(obj.addTwoNumbers(None, obj2.start))


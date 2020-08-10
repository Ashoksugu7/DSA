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

    def traverse(self):
        res=[]
        p =self.start
        while p is not None:
            res.append(p.val)
            p=p.next
        return res
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        p = self.start
        i=0
        while p is not None:
            if i == index:
                return p.val
            p=p.next
            i+=1

        return -1
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        temp = Node(val)
        temp.next = self.start
        self.start = temp 
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        #temp=Node(val)
        p=self.start
        while p.next is not None:
            p=p.next
        p.next=Node(val)


        
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        p=self.start
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
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        p=self.start
        if index == 0:            
            self.start = self.start.next

        i=1
        while p.next is not None:
            if i == index:
                p.next = p.next.next
                break
            p=p.next
            i+=1

        


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
# param_1 = obj.get(index)
obj.addAtHead(2)
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1, -1)
obj.deleteAtIndex(2)
print("Traversal", obj.traverse())
print("Get value from index:", obj.get(2))
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)  
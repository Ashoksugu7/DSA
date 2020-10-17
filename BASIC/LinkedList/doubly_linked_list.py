class Node:
    def __init__(self, val):
        self.val=val
        self.next=None
        self.prev=None

class Doubly:
    def __init__(self):
        self.start=None
        self.count=0

    def addAtHead(self, val):
        temp=Node(val)
        if self.start is None:
            self.start = temp
        else:
            temp.next=self.start
            self.start.prev=temp
            self.start=temp
        
        self.count+=1

        return True
    
    def addAtTail(self,val):
        if self.start is None:
            return self.addAtHead(val)
        
        p = self.start
        while p.next is not None:
            p=p.next
        temp=Node(val)
        p.next=temp
        temp.prev=p

        self.count+=1
        return True

    def addAtIndex(self, index, val):
        if index==0:
            return self.addAtHead(val)

        if index==-1 or index >= self.count:
            return self.addAtTail(val)

        p=self.start
        i=0
        while i < index-1:
            p=p.next            
            i+=1
        temp=Node(val)
        temp.prev=p
        temp.next=p.next
        p.next.prev=temp
        p.next=temp


        self.count+=1
        return True

    def get(self, index):
        if index > self.count-1:
            return -1
        i=0
        p=self.start
        
        while i < index:
            
            i+=1
            p=p.next

        return p.val

    def deleteAtHead(self):
        if self.start is None:
            return -1

        if self.count ==1:
            self.start=None
            self.count-=1
            return True
        
        self.start=self.start.next
        self.start.prev=None

        self.count-=1
        return True

    def deleteAtTail(self):
        if self.start is None:
            return -1

        if self.count==1:
            return self.deleteAtHead()

        p=self.start
        while p.next.next is not None:
            p=p.next
        
        p.next.prev=None
        p.next=None

        self.count-=1
        return True
    
    def deleteAtIndex(self, index):
        if index >= self.count:
            return False

        if index==0:
            return self.deleteAtHead()
        
        if index == -1 or index==self.count-1:
            return self.deleteAtTail()
        
        p=self.start
        i=0
        while i < index-1:
            p=p.next
            i+=1

        p.next=p.next.next
        p.next.prev=p

        self.count-=1
        return True
        
    def traversal(self):
        res=[]
        if self.start is None:
            return -1

        p = self.start
        while p is not None:
            res.append(p.val)
            p=p.next

        return res
            

obj = Doubly()
obj.addAtHead(4)
obj.get(1)
obj.addAtHead(1)
obj.addAtHead(5)

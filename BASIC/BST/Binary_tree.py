class Node:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self):
        self.root=None

    def pre_order(self, p):
        if p is None:
            return 
        print(p.val, end=" ")
        self.pre_order(p.left)
        self.pre_order(p.right)


    def _pre_order(self):
        self.pre_order(self.root)
        print(" ")


    def _in_order(self):
        self.in_order(self.root)
        print(" ")

    def in_order(self, p):
        if p is None:
            return
        
        self.in_order(p.left)
        print(p.val, end=" ")
        self.in_order(p.right)

    def _post_order(self):
        self.post_order(self.root)
        print(" ")

    def post_order(self, p):
        if p is None:
            return

        self.post_order(p.left)
        self.post_order(p.right)
        print(p.val, end=" ")

    def iterative_inorder(self):
        stack=[]
        p=self.root
        while len(stack)!= 0 or p is not None:
            if p is not None:
                stack.append(p)
                p=p.left
            else:
                p=stack.pop()
                print(p.val, end=" ")
                p=p.right

        print(" ")


    def iterative_preorder(self):
        stack=[]
        p=self.root

        while len(stack)!=0 or p is not None:
            if p is not None:
                stack.append(p)
                print(p.val, end=" ")
                p=p.left

            else:
                p=stack.pop()
                p=p.right
        
        print(" ")


    
    def iterative_postorder_twostack(self):
        stack1=[]
        stack2=[]
        p=self.root
        stack1.append(p)

        while len(stack1)!=0:
            temp=stack1.pop()
            stack2.append(temp)

            if temp.left is not None:
                stack1.append(temp.left)
            
            if temp.right is not None:
                stack1.append(temp.right)

        while len(stack2)!=0:
            temp=stack2.pop()
            print(temp.val, end=" ")

        print(" ")


    def iterative_postorder_onestack(self):
        current=self.root
        stack=[]
        while len(stack)!=0 or current is not None:
            if current is not None:
                 stack.append(current)
                 current=current.left
            else:
                temp = stack[-1].right
                if temp is None:
                    temp=stack.pop()
                    print(temp.val, end=" ")
                    while( len(stack)!=0 and temp==stack[-1].right):
                        temp=stack.pop()
                        print(temp.val, end=" ")

                else:
                    current=temp

        print(" ")




        






    
obj=BinaryTree()
obj.root = Node(1)
obj.root.left=Node(2)
obj.root.right = Node(3)
obj.root.left.left=Node(4)
obj.root.left.right=Node(5)
obj.root.right.left=Node(6)
obj.root.right.right=Node(7)
obj.root.right.right.right=Node(8)


print("PRE-ORDER: ",obj._pre_order())
print("IN-ORDER: ",obj._in_order())
print("POST-ORDER: ",obj._post_order())

print("IN-ORDER ITERATIVE: ", obj.iterative_inorder())
print("PRE-ORDER ITERATIVE: ", obj.iterative_preorder())
print("POST-ORDER ITERATIVE USING ONE STACK: ", obj.iterative_postorder_twostack())
print("POST-ORDER ITERATIVE USING TWO STACK: ", obj.iterative_postorder_onestack())
"""
Design Front Middle Back Queue
User Accepted:0
User Tried:0
Total Accepted:0
Total Submissions:0
Difficulty:Medium
Design a queue that supports push and pop operations in the front, middle, and back.

Implement the FrontMiddleBack class:

FrontMiddleBack() Initializes the queue.
void pushFront(int val) Adds val to the front of the queue.
void pushMiddle(int val) Adds val to the middle of the queue.
void pushBack(int val) Adds val to the back of the queue.
int popFront() Removes the front element of the queue and returns it. If the queue is empty, return -1.
int popMiddle() Removes the middle element of the queue and returns it. If the queue is empty, return -1.
int popBack() Removes the back element of the queue and returns it. If the queue is empty, return -1.
Notice that when there are two middle position choices, the operation is performed on the frontmost middle position choice. For example:

Pushing 6 into the middle of [1, 2, 3, 4, 5] results in [1, 2, 6, 3, 4, 5].
Popping the middle from [1, 2, 3, 4, 5, 6] returns 3 and results in [1, 2, 4, 5, 6].
Input:
["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
[[], [1], [2], [3], [4], [], [], [], [], []]
Output:
[null, null, null, null, null, 1, 3, 4, 2, -1]

Explanation:
FrontMiddleBackQueue q = new FrontMiddleBackQueue();
q.pushFront(1);   // [1]
q.pushBack(2);    // [1, 2]
q.pushMiddle(3);  // [1, 3, 2]
q.pushMiddle(4);  // [1, 4, 3, 2]
q.popFront();     // return 1 -> [4, 3, 2]
q.popMiddle();    // return 3 -> [4, 2]
q.popMiddle();    // return 4 -> [2]
q.popBack();      // return 2 -> []
q.popFront();     // return -1 -> [] (The queue is empty)
"""

class FrontMiddleBackQueue:

    def __init__(self):
        self.fmbQueue = []
        

    def pushFront(self, val: int) -> None:
        self.fmbQueue.insert(0, val)
        

    def pushMiddle(self, val: int) -> None:
        self.fmbQueue.insert(len(self.fmbQueue)//2, val)

    def pushBack(self, val: int) -> None:
        self.fmbQueue.append(val)

    def popFront(self) -> int:
        if len(self.fmbQueue) > 0:
            return self.fmbQueue.pop(0)
        
        return -1
        

    def popMiddle(self) -> int:
        if len(self.fmbQueue) > 0:
            if len(self.fmbQueue)%2==0:
                return self.fmbQueue.pop(len(self.fmbQueue)//2-1)
            else:
                return  self.fmbQueue.pop(len(self.fmbQueue)//2)
            
            
        return -1
        

    def popBack(self) -> int:
        if len(self.fmbQueue) > 0:
            return self.fmbQueue.pop()
        
        return -1
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
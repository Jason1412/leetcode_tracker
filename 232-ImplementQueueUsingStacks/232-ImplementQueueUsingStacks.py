# Last updated: 5/16/2026, 12:28:47 PM
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack1.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.stack1) > 0:
            self.move()
        return self.stack2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.stack1) > 0:
            self.move()
        return self.stack2[-1]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.stack1) > 0:
            self.move()
            
        if len(self.stack2) == 0:
            return True
        else:
            return False
        
    def move(self):
        
        if not self.stack2:
            
            while(len(self.stack1) > 0):
                tmp = self.stack1.pop()
                self.stack2.append(tmp)
        
         
        

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
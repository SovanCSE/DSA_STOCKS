#################################################################################
## Category: Stack
## Title: Design a stack that supports push, pop, top, retrieve the minimum element in constant time.
## Short notes -
## MinStack initializes the stack object
## void push(val) pushes the element value onto the stack
## void pop() removes the element on top of th stack
## int top() gets the top element from the stack
## int getMin() gets the minimum element in the stack
## Youtube Link: https://www.youtube.com/watch?v=qkLl7nAwDPo&list=PLot-Xpze53leF0FeHz2X0aG3zd0mr1AW_&index=6&ab_channel=NeetCode
## Input: ['MinStack', 'push', 'push', 'push', 'getMin' ,  'pop', 'top', 'getMin']
#         [[], [-2], [0], [-3], [], [], [], []]
## Output: [null, null, null, null, -3, null, 0, -2]
##################################################################################

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else -100

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else -100


min_stack = MinStack()
print(min_stack.push(-2))
print(min_stack.push(0))
print(min_stack.push(-1))
#End of the above following operations -  stack = [-2, 0, -1] and min_stack = [-2, -2, -2]
print(min_stack.getMin())
print(min_stack.pop())
print(min_stack.top()) ## [-2, 0]
print(min_stack.getMin()) ## [-2, -2]

class MyQueue:

    def __init__(self):
        self.stack = []
        self.front = 0
        

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop(self.front)
        self.front += 1
        

    def peek(self) -> int:
        return self.stack[self.front]
        

    def empty(self) -> bool:
        return len(self.stack) == 0

## Method 2
class MyQueue2:
    def __init__(self):
        self.instack = []
        self.outstack = []

    def push(self, x):
        self.instack.append(x)
    
    def pop(self):
        self.move()
        return self.outstack.pop()
    
    def peek(self):
        self.move()
        return self.outstack[-1]
    
    def empty(self):
        return (not self.instack) and (not self.outstack)
    
    def move(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())

class MinStack:

    def __init__(self):
        self.stack = deque()
        self.mins  = deque()
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mins or val<=self.mins[-1]:
            self.mins.append(val)
        

    def pop(self) -> None:
        temp = self.stack.pop()
        if temp==self.mins[-1]:
            self.mins.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.mins[-1]
class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque()
        self.window_size = size
        self.curr_sum = 0
        

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.curr_sum+=val

        if len(self.queue)>self.window_size:
            self.curr_sum -= self.queue.popleft()
        
        return self.curr_sum/len(self.queue)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

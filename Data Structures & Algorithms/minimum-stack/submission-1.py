class MinStack:

    def __init__(self):
        self.s = []
        self.min_val = []
        

    def push(self, val: int) -> None:
        self.s.append(val) 
        if not self.min_val: 
            self.min_val.append(val) 
        else:
            if val < self.min_val[-1]:
                self.min_val.append(val)
            else:
                self.min_val.append(self.min_val[-1]) 
            #self.min_val.append(min(val, self.min_val[-1]))
        

    def pop(self) -> None:
        self.min_val.pop() 
        return self.s.pop()
        

    def top(self) -> int:
        return self.s[-1]
        

    def getMin(self) -> int:
        return self.min_val[-1]
        

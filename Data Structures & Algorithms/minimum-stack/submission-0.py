class MinStack:

    def __init__(self):
        self.i_min = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.i_min) == 0:
            self.i_min.append(0)
        elif  val < self.stack[self.i_min[-1]]:
            self.i_min.append(len(self.stack) - 1)
        else:
            self.i_min.append(self.i_min[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.i_min.pop()

    def top(self) -> int:
        return self.stack[-1]        

    def getMin(self) -> int:
        return self.stack[self.i_min[-1]]
        

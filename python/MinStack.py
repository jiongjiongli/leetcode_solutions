

class MinStack:

    def __init__(self):
        self.data = []
        self.min_index_list = []

    def push(self, val: int) -> None:
        if (not self.min_index_list) or val < self.data[self.min_index_list[-1]]:
            self.min_index_list.append(len(self.data))

        self.data.append(val)

    def pop(self) -> None:
        if self.min_index_list and self.min_index_list[-1] == len(self.data) - 1:
            self.min_index_list.pop()

        val = self.data.pop()

        return val

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.data[self.min_index_list[-1]]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

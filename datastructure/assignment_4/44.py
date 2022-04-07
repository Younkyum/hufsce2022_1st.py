class QueueCircular:
    def __init__(self, count=10):
        self.front = 0
        self.rear = 0
        self.count = count
        self.items = [None] * self.count

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return self.front == (self.rear + 1) % self.count

    def put_in(self, data):
        if not self.is_full():
            self.rear = (self.rear + 1) % self.count
            self.items[self.rear] = data
        else:
            self.items = self.items + ([None] * self.count)
            self.count += self.count
            self.rear = (self.rear + 1) % self.count
            self.items[self.rear] = data

    def put_out(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.count
            return self.items[self.front]

stack = QueueCircular()
stack.put_in(5)
stack.put_in(6)
stack.put_in(7)

print(stack.put_out())
print(stack.put_out())
print(stack.put_out())
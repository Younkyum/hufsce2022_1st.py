class QueueCircular:
    def __init__(self, count=2):
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


def liner(line_, count):
    total = 0
    sum_r = 0
    sum_l = 0
    for _ in range(count):
        person = line_.put_out()
        sum_l += int(person[0])
        if sum_l > sum_r:
            sum_r += sum_l - sum_r
        else:
            total += sum_r - sum_l
        sum_r += int(person[1])
    return total/count


line = QueueCircular()
member = [0, 0]
member_count = int(input())
for i in range(member_count):
    entered = input().split()
    line.put_in(entered)
print("{:.2f}".format(round(liner(line, member_count), 2)))

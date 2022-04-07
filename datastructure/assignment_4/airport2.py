class QueueCircular:
    def __init__(self, count=5):
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


line = QueueCircular()
member_count = int(input())
for i in range(member_count):
    wait, task = map(int, input().split())
    line.put_in([wait, task])

member_1 = line.put_out()
member_2 = line.put_out()

total_wait = 0

desk_1 = member_1[0] + member_1[1]
desk_2 = member_2[0] + member_2[1]
arrive = member_1[0] + member_2[0]

for i in range(member_count - 2):
    member = line.put_out()
    arrive += member[0]
    wait_time = min(desk_1 - arrive, desk_2 - arrive)
    if wait_time >= 0:
        total_wait += wait_time
        if wait_time == (desk_1 - arrive):
            desk_1 += member[1]
        else:
            desk_2 += member[1]
    else:
        if wait_time == (desk_1 - arrive):
            desk_1 += member[1]
        else:
            desk_2 += member[1]
print("{:.2f}".format(round(total_wait / member_count, 2)))

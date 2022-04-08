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
arrive_time = 0
for i in range(member_count):
    wait, task = map(int, input().split())
    arrive_time += wait
    line.put_in([arrive_time, task])
if member_count != 1 and member_count != 2:
    member_1 = line.put_out()
    member_2 = line.put_out()

    f1_ptime = 0
    f2_ptime = 0

    f1_ptime += member_1[0] + member_1[1]
    f2_ptime += member_2[0] + member_2[1]

    total_wait = 0

    for i in range(member_count - 2):
        member_3 = line.put_out()
        waiting_time = min(f1_ptime - member_3[0], f2_ptime - member_3[0])
        if waiting_time < 0:
            if f1_ptime - member_3[0] == waiting_time:
                f1_ptime += abs(waiting_time) + member_3[1]
            else:
                f2_ptime += abs(waiting_time) + member_3[1]
        else:
            if f1_ptime - member_3[0] == waiting_time:
                total_wait += waiting_time
                f1_ptime += member_3[1]
            else:
                total_wait += waiting_time
                f2_ptime += member_3[1]
    print("{:.2f}".format(round(total_wait / member_count, 2)))
else:
    print("{:.2f}".format(0))
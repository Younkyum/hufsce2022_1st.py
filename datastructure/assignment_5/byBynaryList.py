class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DList:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
        self.size = 0

    def select_node(self, index):
        if index == 0:
            return self.head
        elif index == self.size:
            return self.tail
        else:
            target = self.head
            for i in range(index):
                target = target.next
            return target

    def select(self, index):
        return self.select_node(index).data

    def append_right(self, data):
        new_node = Node(data, prev=self.tail)
        self.tail.next = new_node
        self.tail = self.tail.next

    def insert(self, index, data):
        if index > self.size:
            self.size += 1
            self.append_right(data)
        else:
            target = self.select_node(index - 1)
            target.next = Node(data, prev=target)
            self.tail = target.next


class AddrList:
    def __init__(self):
        self.addrlist = DList("www.hufs.ac.kr")
        self.wentedlist = DList("www.hufs.ac.kr")
        print("www.hufs.ac.kr")
        self.currentIndex = 0
        self.totalIndex = 0
        self.totalCount = 0

    def go(self, addr):
        print(addr)
        self.wentedlist.append_right(addr)
        self.totalCount += 1
        self.totalIndex += 1
        self.currentIndex += 1
        self.addrlist.insert(self.currentIndex, addr)
        if self.currentIndex != self.totalIndex:
            self.addrlist.select_node(self.currentIndex).next = None
            self.addrlist.tail = self.addrlist.select_node(self.currentIndex)
            self.totalIndex = self.currentIndex

    def forward(self):
        if self.totalIndex != self.currentIndex:
            self.currentIndex += 1
            print(self.addrlist.select(self.currentIndex))
        else:
            print()

    def backward(self):
        if self.currentIndex > 0:
            self.currentIndex -= 1
            print(self.addrlist.select(self.currentIndex))
        else:
            print()

    def history(self):
        already_printed = []
        for i in range(self.totalCount + 1):
            print_addr = self.wentedlist.select(self.totalCount - i)
            if print_addr not in already_printed:
                already_printed.append(print_addr)
                print(print_addr)

    def quit(self):
        return True

addr_list = AddrList()
while True:
    user_input = input().split()
    if "go" == user_input[0]:
        addr_list.go(user_input[1])
    elif "forward" == user_input[0]:
        addr_list.forward()
    elif "backward" == user_input[0]:
        addr_list.backward()
    elif "history" == user_input[0]:
        addr_list.history()
    elif "show" == user_input[0]:
        print(addr_list.addrlist)
    else:
        break
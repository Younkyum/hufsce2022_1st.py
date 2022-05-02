class PyList:
    def __init__(self):
        self.addrlist = ["www.hufs.ac.kr"]
        self.wented_list = ["www.hufs.ac.kr"]
        print("www.hufs.ac.kr")
        self.currentIndex = 0
        self.totalIndex = 0
        self.totalCount = 0

    def go(self, addr):
        print(addr)
        self.wented_list.append(addr)
        self.totalCount += 1
        self.totalIndex += 1
        self.currentIndex += 1
        self.addrlist.insert(self.currentIndex, addr)
        if self.currentIndex != self.totalIndex:
            del self.addrlist[self.currentIndex + 1:]
            self.totalIndex = self.currentIndex

    def forward(self):
        if self.totalIndex != self.currentIndex:
            self.currentIndex += 1
            print(self.addrlist[self.currentIndex])
        else:
            print()


    def backward(self):
        if self.currentIndex > 0:
            self.currentIndex -= 1
            print(self.addrlist[self.currentIndex])
        else:
            print()

    def history(self):
        already_printed = []
        for i in range(self.totalCount + 1):
            print_addr = self.wented_list[self.totalCount - i]
            if print_addr not in already_printed:
                already_printed.append(print_addr)
                print(print_addr)

    def quit(self):
        return True


addr_list = PyList()
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
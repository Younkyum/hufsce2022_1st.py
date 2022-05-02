class Site:
    def __init__(self):
        self.addrList = ['www.hufs.ac.kr']
        self.cur_ind = 0
        self.cur_site = self.addrList[-1]
        if len(self.addrList) == 1: print(self.addrList[0])

    def go(self, addr):
        self.addrList.append(addr)
        print(addr)
        self.cur_ind += 1
        self.cur_site = addr

    def backward(self):
        if self.cur_ind == 0:
            return
        else:
            self.cur_ind -= 1
            self.cur_site = self.addrList[self.cur_ind]
            print(self.cur_site)

    def forward(self):
        self.cur_ind += 1
        if self.cur_ind > len(self.addrList) - 1:
            self.cur_ind -= 1
            return
        else:
            self.cur_site = self.addrList[self.cur_ind]
            print(self.cur_site)

    def history(self):
        result = list(reversed(self.addrList))
        result = list(dict.fromkeys(result))
        for i in result:
            print(i)

    def quit(self):
        exit(0)


site = Site()

while True:
    command = input().split()
    if 'quit' in command:
        site.quit()
    elif 'go' in command:
        addr = ''
        for i in range(1, len(command)):
            addr += command[i]
        if addr == '': continue
        site.go(addr)
    elif 'backward' in command:
        site.backward()
    elif 'forward' in command:
        site.forward()
    elif 'history' in command:
        site.history()
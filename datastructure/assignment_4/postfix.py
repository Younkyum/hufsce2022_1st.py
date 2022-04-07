class Node:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            return -1
        data = self.head.data
        self.head = self.head.next
        return data

    def is_empty(self):
        if self.head:
            return False
        return True

    def print_all(self):
        if not self.is_empty():
            node = self.head
            print('[', end='')
            while node.next:
                print(node.data, end=', ')
                node = node.next
            print(node.data, ']', sep='')


op = ['+', '–', '*', '//', '%']
num_stack = Stack()
entered = input().split()
total = 0
for i in entered:
    if i == ';':
        break
    elif i not in op:
        num_stack.push(int(i))
    else:
        try:
            first_pop = num_stack.pop()
            second_pop = num_stack.pop()
            if i == '+':
                num_stack.push(first_pop + second_pop)
            elif i == '–':
                num_stack.push(second_pop - first_pop)
            elif i == '*':
                num_stack.push(first_pop * second_pop)
            elif i == '//':
                num_stack.push(second_pop // first_pop)
            elif i == '%':
                num_stack.push(second_pop % first_pop)
            else:
                print("error")
        except:
            print("error")
            break

total = num_stack.pop()
if num_stack.is_empty():
    print(total)
else:
    print("error")

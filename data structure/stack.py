class Stack:

    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__top = -1

    def is_full(self):
        if (self.__top == self.__max_size - 1):
            return True
        return False

    def is_empty(self):
        if (self.__top == -1):
            return True
        return False

    def push(self, data):
        if (self.is_full()):
            print("~ The stack is full! ~")
        else:
            self.__top += 1
            self.__elements[self.__top] = data

    def pop(self):
        if (self.is_empty()):
            print("~ The stack is empty ~")
        else:
            data = self.__elements[self.__top]
            self.__top -= 1
            return data

    def display(self):
        if (self.is_empty()):
            print("~ the stack is empty ~")
        else:
            print("Current stack")
            index = self.__top
            while (index >= 0):
                print(self.__elements[index], end=' ')
                index -= 1
            print()


stack = Stack(4)
# push
print("Is stack empty",stack.is_empty())
stack.push(1)
stack.push(2)
# stack.push(3)
# stack.push(5)

print(stack.pop())
stack.display()

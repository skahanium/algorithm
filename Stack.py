class Stack1:
    '''
    创建一个尾端栈顶的空栈，不包含任何数据项。
    特性：反转次序、后进先出。
    方法：
    （1）isEmpty()
    （2）push(item)
    （3）pop()
    （4）peek()
    （5）size()
    '''

    def __init__(self):
        '''
        初始化
        '''
        self.items = []

    def isEmpty(self):
        '''
        返回是否为空栈
        '''
        return self.items == []

    def push(self, item):
        '''
        将item加入栈顶，无返回值
        '''
        self.items.append(item)

    def pop(self):
        '''
        将栈顶数据移除，并返回。栈被修改。
        '''
        return self.items.pop()

    def peek(self):
        '''
        返回栈顶数据项，但不移除。栈不被修改。
        '''
        return self.items[len(self.items) - 1]

    def size(self):
        '''
        返回栈中有多少个数据项
        '''
        return len(self.items)


class Stack2:
    '''
    创建一个首端栈顶的空栈，其性质与Stack1相同
    '''

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

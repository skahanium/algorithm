class Queue:
    '''
    创建一个空队列，不需要任何参数。
    特性：先进先出，保持顺序。
    方法：
    （1）enqueue(item)
    （2）dequeue()
    （3）isEmpty()
    （4）size()
    '''

    def __init__(self) -> None:
        '''
        初始化
        '''
        self.items = []

    def isEmpty(self):
        '''
        检查队列是否为空。它不需要参数，且会返回一个布尔值。
        '''
        return self.items == []

    def enqueue(self, item):
        '''
        在队列的尾部添加一个元素。它需要一个元素作为参数，不返回任何值。
        '''
        self.items.insert(0, item)

    def dequeue(self):
        '''
        从队列的头部移除一个元素。它不需要参数，且会返回一个元素，并修改队列的内容。
        '''
        return self.items.pop()

    def size(self):
        '''
        返回队列中元素的数目。它不需要参数，且会返回一个整数。
        '''
        return len(self.items)

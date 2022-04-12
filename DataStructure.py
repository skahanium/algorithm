from typing import Any


class Stack:
    def __init__(self):
        """初始化栈，得到一个空栈。

        Returns:
            List: 空栈
        """
        self.items = []

    def isEmpty(self) -> bool:
        """检查栈是否为空，无需参数，返回布尔值。

        Returns:
            Bool: 检查结果
        """
        return self.items == []

    def push(self, item: Any) -> None:
        """将一个新项添加到栈顶，需要item作为参数，不返回任何值。

        Args:
            item (Any): 新增项
        """
        self.items.append(item)

    def pop(self) -> Any:
        """从栈中删除顶部项，无需参数并返回顶部项，同时栈被修改。

        Returns:
            Any: 原顶部项
        """
        return self.items.pop()

    def peek(self) -> Any:
        """从栈返回顶部项，但不删除它。无需参数，不修改栈。

        Returns:
            Any: 栈顶部项
        """
        return self.items[len(self.items) - 1]

    def size(self) -> int:
        """返回栈的大小，无需参数，不修改栈。

        Returns:
            Int: 栈大小
        """
        return len(self.items)


class Queue:
    def __init__(self):
        """初始化队列，得到一个空队列。

        Returns:
            List: 空队列
        """
        self.items = []

    def isEmpty(self) -> bool:
        """检查队列是否为空，无需参数，返回布尔值。

        Returns:
            Bool: 检查结果
        """
        return self.items == []

    def enqueue(self, item: Any) -> None:
        """将一个新项添加到队列尾部，需要item作为参数，不返回任何值。

        Args:
            item (Any): 新增项
        """
        self.items.insert(0, item)

    def dequeue(self) -> Any:
        """从队列中删除队首项，无需参数并返回队首项，同时队列被修改。

        Returns:
            Any: 原队首项
        """
        return self.items.pop()

    def size(self) -> int:
        """返回队列的大小，无需参数，不修改队列。

        Returns:
            Int: 队列大小
        """
        return len(self.items)


class Deque:
    def __init__(self):
        """初始化双端队列，得到一个空双端队列。

        Returns:
            List: 空双端队列
        """
        self.items = []

    def isEmpty(self) -> bool:
        """检查双端队列是否为空，无需参数，返回布尔值。

        Returns:
            Bool: 检查结果
        """
        return self.items == []

    def addFront(self, item: Any) -> None:
        """将一个新项添加到双端队列头部，需要item作为参数，不返回任何值。

        Args:
            item (Any): 新增项
        """
        self.items.append(item)

    def addRear(self, item: Any) -> None:
        """将一个新项添加到双端队列尾部，需要item作为参数，不返回任何值。

        Args:
            item (Any): 新增项
        """
        self.items.insert(0, item)

    def removeFront(self) -> Any:
        """从双端队列中删除队首项，无需参数并返回队首项，同时双端队列被修改。

        Returns:
            Any: 原队首项
        """
        return self.items.pop()

    def removeRear(self) -> Any:
        """从双端队列中删除队尾项，无需参数并返回队尾项，同时双端队列被修改。

        Returns:
            Any: 原队尾项
        """
        return self.items.pop(0)

    def size(self) -> int:
        """返回双端队列的大小，无需参数，不修改双端队列。

        Returns:
            Int: 双端队列大小
        """
        return len(self.items)


class Node:
    def __init__(self, initdata: Any, next: Any = None):
        """初始化节点，得到一个节点。

        Args:
            data (Any): 节点数据
            next (Any): 下一个节点
        """
        self.data = initdata
        self.next = next

    def getData(self) -> Any:
        """返回节点数据，无需参数，不修改节点。

        Returns:
            Any: 节点数据
        """
        return self.data

    def getNext(self) -> Any:
        """返回下一个节点，无需参数，不修改节点。

        Returns:
            Any: 下一个节点
        """
        return self.next

    def setData(self, newdata: Any) -> None:
        """修改节点数据，需要newdata作为参数，不返回任何值。

        Args:
            newdata (Any): 新数据
        """
        self.data = newdata

    def setNext(self, newnext: Any) -> None:
        """修改下一个节点，需要newnext作为参数，不返回任何值。

        Args:
            newnext (Any): 新下一个节点
        """
        self.next = newnext


class UnorderedList:
    def __init__(self):
        """初始化无序链表，得到一个空无序链表。

        Returns:
            List: 空无序链表
        """
        self.head = None

    def isEmpty(self) -> bool:
        """检查无序链表是否为空，无需参数，返回布尔值。

        Returns:
            Bool: 检查结果
        """
        return self.head is None

    def add(self, item: Any) -> None:
        """将一个新项添加到无序链表，需要item作为参数，不返回任何值。

        Args:
            item (Any): 新增项
        """
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self) -> int:
        """返回无序链表的大小，无需参数，不修改无序链表。

        Returns:
            Int: 无序链表大小
        """
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item: Any) -> bool:
        """查找无序链表中是否存在项item，需要item作为参数，返回布尔值。

        Args:
            item (Any): 查找项

        Returns:
            Bool: 查找结果
        """
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item: Any) -> None:
        """从无序链表中删除项item，需要item作为参数，不返回任何值。

        Args:
            item (Any): 删除项
        """
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


class OrderedList:
    def __init__(self):
        """初始化有序链表，得到一个空有序链表。

        Returns:
            List: 空有序链表
        """
        self.head = None

    def isEmpty(self) -> bool:
        """检查有序链表是否为空，无需参数，返回布尔值。

        Returns:
            Bool: 检查结果
        """
        return self.head is None

    def size(self) -> int:
        """返回有序链表的大小，无需参数，不修改有序链表。

        Returns:
            Int: 有序链表大小
        """
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item: Any) -> bool:
        """查找有序链表中是否存在项item，需要item作为参数，返回布尔值。

        Args:
            item (Any): 查找项

        Returns:
            Bool: 查找结果
        """
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            elif current.getData() > item:
                stop = True
            else:
                current = current.getNext()
        return found

    def add(self, item: Any) -> None:
        """将一个新项添加到有序链表，需要item作为参数，不返回任何值。

        Args:
            item (Any): 新增项
        """
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        temp = Node(item)
        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def remove(self, item: Any) -> None:
        """从有序链表中删除项item，需要item作为参数，不返回任何值。

        Args:
            item (Any): 删除项
        """
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

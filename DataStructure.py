class Stack:
    def __init__(self):
        """初始化栈，返回一个空栈。

        Returns:
            List: 空栈
        """
        self.items = []

    def isEmpty(self):
        """检查栈是否为空，无需参数，返回布尔值。

        Returns:
            Bool: 检查结果
        """
        return self.items == []

    def push(self, item):
        """将一个新项添加到栈顶，需要item作为参数，不返回任何值。

        Args:
            item (Any): 新增项
        """
        self.items.append(item)

    def pop(self):
        """从栈中删除顶部项，无需参数并返回顶部项，同时栈被修改。

        Returns:
            Any: 原顶部项
        """
        return self.items.pop()

    def peek(self):
        """从栈返回顶部项，但不删除它。无需参数，不修改栈。

        Returns:
            Any: 栈顶部项
        """
        return self.items[len(self.items) - 1]

    def size(self):
        """返回栈中item的数量，不需要参数，并返回一个整数。

        Returns:
            Int: 栈中item的数量
        """
        return len(self.items)

from Stack import Stack1


def ten2two(decNumber):
    remstack = Stack1()
    teststack = Stack1()
    optional_objects = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    test = decNumber
    while test > 0:
        rem = test % 10
        teststack.push(rem)
        test = test // 10

    while not teststack.isEmpty():
        opt = teststack.pop()
        if opt not in optional_objects:
            print('无效输入！')
            exit()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString


def two2ten(decNumber):
    remstack = Stack1()

    while decNumber > 0:
        rem = decNumber % 10
        remstack.push(rem)
        decNumber = decNumber // 10

    binString = 0
    i = 1
    length = remstack.size()
    while not remstack.isEmpty():
        binString = binString + remstack.pop() * (2 ** (length-i))
        i = i + 1

    return binString

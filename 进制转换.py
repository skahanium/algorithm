from Stack import Stack1


def ten2two(decNumber):
    remstack = Stack1()

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


s = two2ten
print(s(111))

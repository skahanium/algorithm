def classify_1(obj1, obj2):
    result1 = list(obj1)
    result2 = list(obj2)
    m = len(result1)
    n = len(result2)
    for i in range(m):
        for j in range(n):
            if result1[i] == result2[j]:
                result2[j] = ''
    tool = ''
    seq = tool.join(result2)
    if seq == '':
        print('Yes!')
    else:
        print('No!')



def classify_2(obj1, obj2):
    result1 = list(obj1)
    result2 = list(obj2)
    if result1.sort() == result2.sort():
        print('Yes!')
    else:
        print('No!')



def classify_3(obj1, obj2):
    result1 = list(obj1)
    result2 = list(obj2)
    result1_set = list(set(result1))
    result2_set = list(set(result2))
    count1 = {}
    count2 = {}
    for i in range(len(result1_set)):
        for j in range(len(result1)):
            number1 = 0
            if result1_set[i] == result1[j]:
                number1 += 1
                count1[result1_set[i]] = number1
    for m in range(len(result2_set)):
        for n in range(len(result2)):
            number2 = 0
            if result2_set[m] == result2[n]:
                number2 += 1
                count2[result2_set[m]] = number2
    if count1 == count2:
        print('Yes!')
    else:
        print('No!')
    
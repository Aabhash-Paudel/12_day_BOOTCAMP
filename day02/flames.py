def count(str1, str2):
    list1 = list(str1)
    list2 = list(str2)
    for val in list1:
        for v in list2:
            if val == v:
                list1.remove(v)
                list2.remove(v)
    count = len(list2) + len(list1)
    return count


def flames(c):
    flames = list("flames")
    flag = 0
    while len(flames) > 1:
        flag = (c - 1 + flag) % len(flames)
        flames.pop(flag)
    return flames[0]


name1 = "raju"
name2 = "pavi"
print(flames(count(name1, name2)))

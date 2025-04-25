def abc(a):
    if a == 4:
        return
    a += 1
    abc(a)  # a = 2
    print("CSE", end=" ")
    abc(a)
    print("MECH", end=" ")


def main():
    num = "1"
    for a in num:
        print()
        abc(int(a))


main()

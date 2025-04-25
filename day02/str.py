"""
input = aaaabbbccaddd
output = a4b3c2a1d3
"""


def huffman(s):
    res = ""
    count = 1
    for i in range(len(s)):
        if i <= len(s) - 2 and s[i] == s[i + 1]:
            count += 1
        else:
            res = res + s[i]
            res = res + str(count)
            count = 1
    print(res)


huffman("aaaaggggaaadfgasss")

def abc(word):
    a = 1
    words = ""
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            a += 1
        else:
            words += word[i] + str(a)
            a = 1
    words += word[-1] + str(a)
    return words

word = "aaabbacccd"
print(abc(word))

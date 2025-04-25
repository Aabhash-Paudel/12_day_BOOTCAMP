def isValid(s):
    stack = []
    pairs = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char not in pairs:
            stack.append(char)
            continue
        if not stack or stack[-1] != pairs[char]:
            return False
        stack.pop()

    return len(stack) == 0


print(isValid("{()[]}"))

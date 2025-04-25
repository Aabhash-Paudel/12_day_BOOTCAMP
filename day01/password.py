def isValid(string):
    upperFlag = False
    lowerFlag = False
    charFlag = False
    digitFlag = False
    if len(string) > 8:
        digitFlag = True
    for i in string:
        if i.isupper():
            upperFlag = True
        if i.islower:
            lowerFlag = True
        if not i.isalnum():
            charFlag = True
    return upperFlag and lowerFlag and charFlag and digitFlag


if isValid("asdfasfadsfas"):
    print("Strong password")
else:
    print("Weak Password")

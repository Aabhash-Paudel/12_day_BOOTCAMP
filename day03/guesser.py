import random

num = []
while len(num) < 6:
    random_number = random.randrange(10)
    if random_number in num:
        continue
    else:
        num.append(random_number)
print(num)

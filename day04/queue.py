from collections import deque

task = [10, 5, 8]
Q = deque()
num = 0
for i in task:
    num += 1
    d = {"num": i}
    Q.append(d)
    i += 1

time = 4

total = 0
while Q:
    dic = Q.popleft()
    num, task = next(iter(dic.items()))

    if task > time:
        total += time
        task = task - time
        print(f"task {num} runs for {time} : {total}")
    else:
        total += task
        print(f"task runs for {task} : {total}")
        task = task - task
    if task > time:
        Q.append({num, task})

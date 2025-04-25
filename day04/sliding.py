nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
tot = len(nums) - k + 1
maxi = []

for i in range(tot):
    win = nums[:k]
    maxi.append(max(win))
    nums.pop(0)
print(maxi)

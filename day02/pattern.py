"""
1
3 2
4 5 6
0 9 8 7
"""

#
# current_num = 1
# rows = 5
#
# for i in range(1, rows + 1):
#         if rows % 2 == 0:
#             print(current_num, end=" ")
#             current_num += 1
#     for j in range(i):
#         if rows % 2 == 0:
#             print(current_num, end=" ")
#             current_num += 1
#         if rows % 2 == 1:
#             odd.append(current_num)
#     print(odd.reverse())
#     odd = []
#     print()


current_num = 1
rows = 9

for i in range(1, rows + 1):
    if i % 2 == 1:
        for j in range(i):
            print(current_num, end=" ")
            current_num += 1
    if i % 2 == 0:
        nums = []
        for j in range(i):
            nums.append(current_num)
            current_num += 1
        for num in reversed(nums):
            print(num, end=" ")
    print()

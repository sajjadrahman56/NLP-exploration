nums = [1,32,44,53,36,7]

# for i in range(len(nums)):
#     print(f"the current nums is = {nums[i]}")
#     for j in range(len(nums)):
#         print('the name = {nums[i] * 10}')
 
# --------------------------------------------- Example of a nested loop
'''
for i in range(3):  # Outer loop
    for j in range(2):  # Inner loop
        print(f"Nested Loop: i={i}, j={j}")
'''

# -------------------------------------- Example of a quadruple loop
count = 1
for a in range(3):
    for b in range(2):
        for c in range(3):
            for d in range(2):
                print(f"Fourth-Level Loop: a={a}, b={b}, c={c}, d={d} and count is = {count}")
                count +=1

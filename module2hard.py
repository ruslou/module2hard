import random

print('welcome to the dungeon, master!')
print('******************************')
print('if you want to stay alive, you need to solve our puzzle')
print('******************************')

n = list(range(3, 21))
random_n = random.choice(n)
print('left element')
print('************')
print(random_n)
print('*************')
print('right element')
print('*************')
for i in range(1, random_n):
    for k in range(i + 1, random_n):
        m = i + k
        if random_n % m == 0:
            print(i, end='')
            print(k, end='')











import sys

sys.setrecursionlimit(5000)
counter = 0

def recur(num):
    global counter
    if num == 1:
        return True
    if num % 2 == 0:
        num //= 2
    else:
        num = 3 * num + 1
    counter += 1
    recur(num)


max_kolla = -1
for i in range(2, 1000000):
    recur(i)
    if counter > max_kolla:
        max_kolla = i
    counter = 0
print(str(max_kolla))

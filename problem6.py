kv_sum = 0
for i in range (100):
    kv_sum += i
kv_sum *= kv_sum
sum_kv = 0
for i in range (1, 100):
    sum_kv += i*i
print(sum_kv - kv_sum)
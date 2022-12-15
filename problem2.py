summ = 2
fib_ryadn = 3
fib_ryadpred1 = 2
fib_ryadpred2 = 1
while (fib_ryadn < 4000000):
    if (fib_ryadn % 2 == 0):
        summ += fib_ryadn
    fib_ryadn = fib_ryadpred2 + fib_ryadpred1
    fib_ryadpred2 = fib_ryadpred1
    fib_ryadpred1 = fib_ryadn
print(summ)
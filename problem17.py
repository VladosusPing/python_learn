first = {
         1 : "one", 2 : "two", 3 :"three",
         4 :"four", 5 :"five", 6 : "six",
         7 : "seven", 8 :"eight", 9 :"nine",
         10: "ten", 11 :"eleven", 12 : "twelve",
         13 : "thirteen", 14 :"fourteen", 15 : "fifteen",
         16 : "sixteen", 17 : "seventeen", 18 : "eighteen",
         19 : "nineteen"}
second = {0 : "", 2 : "twenty", 3 : "thirty",
          4 : "forty", 5 : "fifty", 6 : "sixty",
          7 : "seventy", 8 : "eighty", 9 : "ninety",
          100 : "hundred", 1000 : "thousand", 666 : "and"}



stroka = []
calc = 0

for i in range (1, 1001):
    if i % 1000 > 100:
        if i % 100 != 0:
            stroka.append(second.get(666))
        stroka.append(first.get((i // 100) % 10))
        stroka.append(second.get(100))
    if i % 100 >= 20:
        if i % 10 == 0:
            stroka.append(second.get((i // 10) % 10))
        else:
            stroka.append(second.get((i // 10) % 10))
            stroka.append(first.get(i % 10))
    if i % 100 < 20:
        stroka.append(first.get(i % 100))

stroka.append(first.get(1))
stroka.append(second.get(1000))

for i in range(len(stroka)):
    calc += len(str(stroka[i]))
print(calc)

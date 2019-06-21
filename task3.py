#! /bin/bash python
n = 1001
while n > 1000:
    print("Please, input number N (N shuld be < 1000)")
    n = int(input())

i = 1
res = 1

while i < n:
    i = i + 1
    res = res * i

print("N!=", res)

#! /bin/bash python

i = 0
base = {}
time = []

student = int(input("please insert sum of students: "))


def pupil(name, f, m, h):
    crz = (int(m) + int(f) + int(h)) / 3
    crz = float('{:.2f}'.format(crz))
    base[name] = m + " " + f + " " + h + " " + str(crz)
    return base


def result(base, nameinp):
    res = (base[nameinp]).split()
    return res[3]


while i < student:
    i += 1
    time = (input("print name and marks ")).split()
    pupil(name=time[0], f=time[1], m=time[2], h=time[3])

nameinp = str(input('Input name: '))

print("average mark", result(base, nameinp))

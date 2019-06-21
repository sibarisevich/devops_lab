#! /bin/bash python
print("Input size")
size = input()
height = int(size.partition(" ")[0])
width = int(size.partition(" ")[2])

hheight = int(height / 2)
hwidth = int(width / 2)
i = 0
printlength = str
while i < hheight:
    printlength = "-" * (hwidth - 1 - i * 3) + ".|." * (i * 2 + 1) + "-" * (hwidth - i * 3 - 1)
    print(printlength)
    i += 1

print("-" * (hwidth - 3) + "WELCOME" + "-" * (hwidth - 3))
i = hheight
while i > 0:
    i -= 1
    printlength = "-" * (hwidth - 1 - i * 3) + ".|." * (i * 2 + 1) + "-" * (hwidth - i * 3 - 1)
    print(printlength)

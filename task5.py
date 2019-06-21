#! /bin/bash python
print ("Input robot path")
robopath = input()
U = D = R = L = 0
U = robopath.count("u")
D = robopath.count("d")
R = robopath.count("r")
L = robopath.count("l")
if (U - D == 0) & (R - L == 0):
    print ("true")
else:
    print ("folse")

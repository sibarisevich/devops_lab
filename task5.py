#! /bin/bash python
print ("Input robot path")
robopath = input()
u=d=r=l=0
u=robopath.count("u")
d=robopath.count("d")
r=robopath.count("r")
l=robopath.count("l")
if (u-d==0) & (r-l==0):
    print ("true")
else:
    print ("folce")

#! /bin/bash python
def gorobotgo(robopath):
    U = D = R = L = 0
    U = robopath.count("u")
    D = robopath.count("d")
    R = robopath.count("r")
    L = robopath.count("l")
    if(U - D == 0) & (R - L == 0):
        return True
    else:
        return False

if __name__ == "__main__":
    robopath = input("Input robot path: ")
    print(gorobotgo(robopath))

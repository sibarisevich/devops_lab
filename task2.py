#! /bin/bash python
join={}
#----------input kee data-----------
kee = []
inp="yes"

print ("please,	insert keewords:")
kee.append(input())

while inp!="no":
	print ("Do you wont input another kee? (sey no fo exit)")
	inp = input()
	if inp=="no":
		break
	else:
		kee.append(inp)


#------------input value data----------
Val = []
inp="yes"

print ("please, insert Values:")
Val.append(input())

while inp!="no":
        print ("Do you wont input another Value? (sey no fo exit)")
        inp = input()
        if inp=="no":
                break
        else:
                Val.append(inp)

def splitfn (key, volume=None):
	"""function for join 2 tables"""
	join[key]=volume
	return join

for i in range(len(kee)):
	if i<len(Val):
		splitfn(key=kee[i], volume=Val[i])
	else:
		splitfn(key=kee[i])

print (join)
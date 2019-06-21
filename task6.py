#! /bin/bash python

m=set(input())
temp=str(input())
m=set(map(int,temp.split()))

n=set(input())
temp=str(input())
n=set(map(int,temp.split()))

print(*sorted(m-n, key=int), sep='\n')

#!/usr/bin/env python3
#Else If statement

print("Enter value for X: ")
x = input()
print("Enter integer value for Y: ")
y = input()

if x < y:
    print(f'x < y: x is {x} and y is {y}')
elif x > y:
    print(f'x > y: x is {x} and y is {y}')
else:
    print(f'x == y: x is {x} and y is {y}')


import sys

def rush(x, y):
    #validate input
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return
    
    #single cell case
    if x == 1 and y == 1:
        print("B")
        return
    
    #single row case
    if y == 1:
        print("B" * x)
        return
    
    #single column case
    if x == 1:
        for _ in range(y):
            print("B")
        return
    
    #general case
    #top row
    print("A" + "B" * (x - 2) + "C")
    
    #middle rows
    for _ in range(y - 2):
        print("B" + " " * (x - 2) + "B")
    
    #bottom row
    print("A" + "B" * (x - 2) + "C")

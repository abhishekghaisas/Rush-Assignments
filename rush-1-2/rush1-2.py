import sys

def rush(x, y):
    #validate input
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return
    
    #single cell case
    if x == 1 and y == 1:
        print("*")
        return
    
    #single row case
    if y == 1:
        print("*" * x)
        return
    
    #single column case
    if x == 1:
        for _ in range(y):
            print("*")
        return
    
    #general case
    #top row
    print("/" + "*" * (x - 2) + "\\")
    
    #middle rows
    for _ in range(y - 2):
        print("*" + " " * (x - 2) + "*")
    
    #bottom row
    print("\\" + "*" * (x - 2) + "/")

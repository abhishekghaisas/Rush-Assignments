import sys

def rush(x, y):
    #validate input
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return
    
    #single cell case
    if x == 1 and y == 1:
        print("o")
        return
    
    #single row case
    if y == 1:
        print("o" + "-" * (x - 2) + "o")
        return
    
    #single column case
    if x == 1:
        print("o")
        for _ in range(y - 2):
            print("|")
        print("o")
        return
    
    #general case
    #top row
    print("o" + "-" * (x - 2) + "o")
    
    #middle rows
    for _ in range(y - 2):
        print("|" + " " * (x - 2) + "|")
    
    #bottom row
    print("o" + "-" * (x - 2) + "o")

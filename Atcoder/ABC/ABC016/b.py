import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    A,B,C = map(int,input().split())
    if A+B == C and A-B == C:
        print("?")
    elif A+B == C:
        print("+")
    elif A-B == C:
        print("-")
    else:
        print("!")

if __name__ == '__main__':
    main()
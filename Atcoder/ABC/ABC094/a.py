import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    A,B,X = map(int,input().split())
    if A > X or A+B < X:
        print("NO")
    else:
        print("YES")

if __name__ == '__main__':
    main()
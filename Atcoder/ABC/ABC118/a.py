import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    A,B = map(int,input().split())
    if B%A == 0:
        print(A+B)
    else:
        print(B-A)

if __name__ == '__main__':
    main()
import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    A,B = map(int,input().split())
    if A-(B*2) < 0:
        print(0)
    else:
        print(A-(B*2))

if __name__ == '__main__':
    main()
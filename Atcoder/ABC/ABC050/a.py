import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    A,op,B = input().split()
    if op == "+":
        print(int(A)+int(B))
    else:
        print(int(A)-int(B))

if __name__ == '__main__':
    main()
import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    A,B,C = map(int,input().split())
    print(max(A,B,C)*10+A+B+C-max(A,B,C))

if __name__ == '__main__':
    main()
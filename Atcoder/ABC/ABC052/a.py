import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    A,B,C,D = map(int,input().split())
    print(max([A*B,C*D]))

if __name__ == '__main__':
    main()
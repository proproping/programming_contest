import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N,K = map(int,input().split())
    print("0") if N%K == 0 else print("1")

if __name__ == '__main__':
    main()
import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    print(N) if N%2 == 0 else print(N*2)

if __name__ == '__main__':
    main()
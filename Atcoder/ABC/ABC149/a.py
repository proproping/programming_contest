import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    S,T = map(str,input().split())
    print(T+S)

if __name__ == '__main__':
    main()
import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    P,Q,R = map(int,input().split())
    print(P+Q+R-max(P,Q,R))

if __name__ == '__main__':
    main()
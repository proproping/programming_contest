import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    A,B,C = map(str,input().split())
    if A[-1] == B[0] and B[-1] == C[0]:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
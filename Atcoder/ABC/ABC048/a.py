import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    a,b,c = map(str,input().split())
    print("A"+str.upper(b[0])+"C")

if __name__ == '__main__':
    main()
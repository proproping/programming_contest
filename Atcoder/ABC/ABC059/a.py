import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    s = list(map(str,input().split()))
    print(str.upper(s[0][0]+s[1][0]+s[2][0]))

if __name__ == '__main__':
    main()
import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    s = input()
    print("".join([s[0]]+[str(len(s[1:-1]))]+[s[-1]]))

if __name__ == '__main__':
    main()
import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    S = list(input())
    if sorted(S) == ["a","b","c"]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
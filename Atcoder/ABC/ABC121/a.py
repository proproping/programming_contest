import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    H,W = map(int,input().split())
    h,w = map(int,input().split())
    print(H*W-h*W-(w*(H-h)))

if __name__ == '__main__':
    main()
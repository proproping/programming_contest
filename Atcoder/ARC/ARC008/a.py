def main():
    import math
    N = int(input())
    print(N//10*100+min(N%10*15,100))

if __name__ == '__main__':
    main()
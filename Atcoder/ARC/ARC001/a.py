def main():
    N = int(input())
    C = str(input())
    a,b,c,d = 0,0,0,0
    for i in C:
        if int(i) == 1:
            a += 1
        elif int(i) == 2:
            b += 1
        elif int(i) == 3:
            c += 1
        else:
            d += 1
    ans = [max(a,b,c,d),min(a,b,c,d)]
    print(*ans,sep=" ")

if __name__ == '__main__':
    main()
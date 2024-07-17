def main():
    n=int(input())
    a=0
    b=1
    print("Fibonacci sequence:")
    print(a,end=" ")
    print(b,end=" ")
    for _ in range(n-2):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
        

if __name__ == "__main__":
    main()

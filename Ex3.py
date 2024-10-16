def median(a, b, c):
    if (b <= a <= c) or (c <= a <= b):
        return a

    if (a <= b <= c) or (c <= b <= a):
        return b

    return c

def main():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))
    result = median(a, b, c)
    print(f"The mid value is: {result}")


if __name__ == "__main__":
    main()


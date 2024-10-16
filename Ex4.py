def prime(n):
    for i in range(2, (n//2) + 1):
        if n % i == 0:
            return False  
    return True  

def main():
    a = int(input("Enter the number: "))
    if prime(a):
        print(f"{a} is a prime number.")
    elif a > 1:
        print(f"{a} is a composite number.")
    else:
        print(f"{a} is neither prime nor composite.")

if __name__ == "__main__":
    main()

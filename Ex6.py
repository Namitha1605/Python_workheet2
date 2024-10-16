
#Write a program that takes two numbers a,b and prints their sum, product, difference, quotient
def sum(a,b):
    return a + b
def diff(a,b):
    return a - b
def product(a,b):
    return a * b
def quotient(a,b):
    return a % b
def remainder(a,b):
    return a // b
def main():
    a = int(input('Enter 1st number: '))
    b = int(input('Enter 2nd number: '))
    add=sum(a,b)
    sub=diff(a,b)
    mult=product(a,b)
    quo=quotient(a,b)
    rem=remainder(a,b)
    print (f" the addition of {a}  and {b} is: {add}")
    print (f" the substraction of {a}  and {b} is: {sub}")
    print (f" the product of {a}  and {b} is: {mult}")
    print (f" the quotient {a}  and {b} is: {quo}")
    print (f" the remainder of {a}  and {b} is: {rem}")
    
if __name__ == "__main__":
    main()  


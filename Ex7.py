
#Write a program that prints the cube and square of a user entered number.
def cube(a):
    return a*a*a
def square(a):
    return a*a
def main():
    a = int(input('Enter a number: '))
    Cube=cube(a)
    Square=square(a)
    print (f" the cube of {a}: {Cube}")
    print (f" the Square of {a} is: {Square}")
   
if __name__ == "__main__":
    main()  


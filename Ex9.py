
#Write a program that takes 3 sides and checks if a triangle can be formed from it. (Apply the triangle inequality law)
def inequality_z(x,y,z):
    return x+y>z
def inequality_y(x,y,z):
    return x+z>y
def inequality_x(x,y,z):
    return z+y>x

def main():
    x=int(input('Enter a number: '))
    y=int(input('Enter a number: '))
    z=int(input('Enter a number: '))
    traingle = (inequality_z(x,y,z) and inequality_x(x,y,z) and inequality_y(x,y,z))
    if traingle:
        print (f" it can form a traingle:")
    else:
        print(f"it cannot form a traingle:")
if __name__ == "__main__":
    main()  


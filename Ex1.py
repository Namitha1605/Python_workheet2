#The volume of a cylinder can be computed by multiplying the area of its circular base by its height. 
#Write a program that reads the radius of the cylinder, along with its height, from the user and computes its volume. 
#Display the result rounded to two decimal places.
def V_Cylinder(r,h):
    return 3.14 * r ** 2 * h
def main():
    r=float(input("Enter the radius of cylinder: "))
    h=float(input("Enter the height of cylinder: "))
    result=V_Cylinder(r,h)
    print(f"the volume of cylinder: {result:2f}")
    
if __name__ == "__main__":
    main()

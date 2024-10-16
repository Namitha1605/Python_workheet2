import math

# Function to compute the hypotenuse using the Pythagorean theorem
def PY_T(a, b):
    return math.sqrt(a**2 + b**2)

def main():
    a = float(input("Enter the length of the first shorter side: "))
    b = float(input("Enter the length of the second shorter side: "))
  
    result = PY_T(a, b)
    
    print(f"The length of the hypotenuse is: {hypotenuse:.2f}")

if __name__ == "__main__":
    main()

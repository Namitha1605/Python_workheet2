def colour(n):
    if n in range(380, 450):
        return "voilet"
    elif n in range(450,495):
        return "blue"
    elif n in range(495,570):
        return "Green"
    elif n in range(570,590):
        return "yellow"
    elif n in range(590,620):
       return "orange"
    elif n in range(620 < 750):
        return "red"
    else:
        return "the wavelength is out of range"
def main():
    n=int(input("Enter the number: "))
    outPut=colour(n)
    print(f"the colour of {n} is: {outPut}")
    
    
if __name__ == "__main__":
    main()
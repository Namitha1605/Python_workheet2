#Write a program that accepts two words separated by a comma and replaces the comma with “and”.
def words(word):
    return word.replace(",","and")
def main():
   sentence = input("Enter two words separated by a comma: ")
   output= words(sentence)
   print(f" the words separated:{output}")
if __name__ == "__main__":
    main()
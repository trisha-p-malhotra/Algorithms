"""
__author__: Trisha P Malhotra
__description__: Algorithms hw 5
"""


def badnessLine():
    M = int(input("enter the maximum number of characters in a line : "))
    str = input("Enter the sentence : ")
    spaces = len(str.split()) - 1
    words = len(str.split())
    print (spaces)
    print (words)
    words = str.split()
    wordCount = len(words) - 1
    print("Your word and letter counts are:")
    for i in words:
        print(len(i))
    str.split()
    print (sum(c.isalpha() for c in str))
    words = len(str.strip(' '))
    n = M - words
    if n < 0:
        print("The number of white spaces at the end of line is greater than the number of characters allowed")
    print (words)
    print("Number of white spaces at the end of line is : ")
    print (n)


if __name__ == "__main__":
    badnessLine()
# int this regular expression program we will make a program which will except a string and then we can do the program
# .strip() function removes the unwanted space between the string


import re

ex = input("Enter an expression:")
with open("string.txt","r") as file:
    lines=file.readlines()
    for line in lines:
        if re.search(ex, line):
            print(f"string '{line.strip()}' Accepted")
        else:
            print(f"string'{line.strip()}' not accepted")
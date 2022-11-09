# Oskar Svedlund
# Teinf-20
# 2022-11-09
# file managment

from random import randint



choice = input(">> ")

if choice == "1":

    filename = input("File name? \n>> ")
    amount = int(input("Amount of characters? \n>> "))
    filename += ".txt"

    with open(filename, "w", encoding="utf-8") as f:

        x = amount - 1
        for r in range(amount):
            number = randint(1,9)
            number = str(number)
            f.write(number)

            if x != 0 or x < 0:
                x -= 1
                f.write("\n")

if choice == "2":

    filename = input("File name\n>> ")
    filename += ".txt"

    with open(filename, "r", encoding="utf-8") as f:

        for count, line in enumerate(f):
            print(line)

    print("total lines", count + 1)
        
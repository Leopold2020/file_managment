# Oskar Svedlund
# TEINF-20
# 2022-11-10
# Niclas solution

from random import randint
from collections import Counter
def generate_numbers():
    filename = input("filename\n>> ")
    amount = int(input("amount\n>> "))
    with open(filename, "w", encoding="utf-8") as f:
        for _ in range(amount):
            random_number = randint(1, 100)
            f.write(str(random_number) + "\n")
    print("File generated")
    return filename

def count_uniques(filepath):
    count_list = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f.readlines():
            count_list.append(int(line.strip("\n")))
    unique_counter = Counter(count_list)
    print(f"amount of unique numbers : {len(unique_counter)}")

    # for item in unique_counter:
    #     print(item, unique_counter[item])

    ordered_counter = dict(sorted(unique_counter.items()))
    for item in ordered_counter:
        print(item, "\t", ordered_counter[item])

def main():
    filepath = generate_numbers()
    count_uniques(filepath)

if __name__ == "__main__":
    main()
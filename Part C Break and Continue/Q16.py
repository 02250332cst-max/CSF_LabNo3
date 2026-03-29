lst = [2, 4, 6, 8, 10]
target = int(input("Searching for: "))

for num in lst:
    if num == target:
        print("Number found")
        break
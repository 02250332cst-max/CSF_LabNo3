def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b if b != 0 else "Error"

while True:
    print("\n1.Add 2.Subtract 3.Multiply 4.Divide 5.Exit")
    choice = int(input("Enter choice: "))

    if choice == 5:
        break

    a, b = map(float, input("Enter two numbers: ").split())

    if choice == 1:
        print("Sum =", add(a, b))
    elif choice == 2:
        print("Difference =", sub(a, b))
    elif choice == 3:
        print("Product =", mul(a, b))
    elif choice == 4:
        print("Quotient =", div(a, b))
    else:
        print("Invalid choice")
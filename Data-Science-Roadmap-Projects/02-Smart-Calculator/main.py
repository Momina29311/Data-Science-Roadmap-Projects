print("==== Smart Calculator ====")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose an operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("\nEnter choice: ")

if choice == "1":
    result = num1 + num2
    symbol = "+"
elif choice == "2":
    result = num1 - num2
    symbol = "-"
elif choice == "3":
    result = num1 * num2
    symbol = "×"
elif choice == "4":
    if num2 == 0:
        print("Result: Division by zero is not allowed.")
        exit()
    result = num1 / num2
    symbol = "÷"
else:
    print("Invalid choice")
    exit()

print(f"\nResult: {num1:.2f} {symbol} {num2:.2f} = {result:.2f}")
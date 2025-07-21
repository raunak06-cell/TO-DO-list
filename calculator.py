def calculator():
    print("🧮 Welcome to the Simple Calculator!")
    
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("❗ Invalid input. Please enter numeric values.")
        return

    print("\nChoose an operation:")
    print("1 ➕ Addition")
    print("2 ➖ Subtraction")
    print("3 ✖️ Multiplication")
    print("4 ➗ Division")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        result = num1 + num2
        op = '+'
    elif choice == '2':
        result = num1 - num2
        op = '-'
    elif choice == '3':
        result = num1 * num2
        op = '*'
    elif choice == '4':
        if num2 == 0:
            print("❗ Cannot divide by zero.")
            return
        result = num1 / num2
        op = '/'
    else:
        print("❗ Invalid choice. Please select 1, 2, 3, or 4.")
        return

    print(f"\n✅ Result: {num1} {op} {num2} = {result}")

# Run the calculator
calculator()

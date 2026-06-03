print("--- Professional Termux Calculator ---")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"The total is: {num1 + num2}")
except ValueError:
    print("❌ Error: You must enter a valid number! Please try again.")


def add(x: float, y: float) -> float:
    """Return x + y."""
    return x + y


def subtract(x: float, y: float) -> float:
    """Return x - y."""
    return x - y


def multiply(x: float, y: float) -> float:
    """Return x * y."""
    return x * y


def divide(x: float, y: float) -> float:
    """Return x / y. Raise ValueError on division by zero."""
    if y == 0:
        raise ValueError("Division by zero")
    return x / y


def calculator() -> None:
    """Interactive CLI calculator."""
    operations = {
        "1": ("+", add),
        "2": ("-", subtract),
        "3": ("*", multiply),
        "4": ("/", divide),
    }

    def print_menu() -> None:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("q. Quit")

    print_menu()

    while True:
        try:
            choice = input("Enter choice (1/2/3/4) or 'q' to quit: ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            break

        if choice == "q":
            break

        if choice not in operations:
            print("Invalid choice. Please enter 1, 2, 3, 4 or q.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            break

        symbol, func = operations[choice]
        try:
            result = func(num1, num2)
        except Exception as e:
            print(f"Error: {e}")
            continue

        # Print result with compact formatting
        try:
            print(f"{num1} {symbol} {num2} = {result:.10g}")
        except Exception:
            # Fallback if result is non-numeric for some reason
            print(f"{num1} {symbol} {num2} = {result}")


if __name__ == "__main__":
    calculator()

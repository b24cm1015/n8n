def add(x: float, y: float) -> float:
    """Return the sum of x and y."""
    return x + y


def subtract(x: float, y: float) -> float:
    """Return the difference x - y."""
    return x - y


def multiply(x: float, y: float) -> float:
    """Return the product of x and y."""
    return x * y


def divide(x: float, y: float) -> float:
    """Return x / y. Raise ValueError on division by zero."""
    if y == 0:
        raise ValueError("Division by zero")
    return x / y


def calculator() -> None:
    """Interactive CLI calculator."""
    operations = {
        "1": ("Add", add, "+"),
        "2": ("Subtract", subtract, "-"),
        "3": ("Multiply", multiply, "*"),
        "4": ("Divide", divide, "/"),
    }

    def print_menu() -> None:
        print("Select operation:")
        for key, (label, _, _) in operations.items():
            print(f"{key}. {label}")
        print("q. Quit")

    while True:
        try:
            print_menu()
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

        _, func, symbol = operations[choice]
        try:
            result = func(num1, num2)
        except ValueError as e:
            print(f"Error: {e}")
            continue
        except Exception as e:
            print(f"Unexpected error: {e}")
            continue

        # Print result with a compact formatting
        try:
            print(f"{num1} {symbol} {num2} = {result:.10g}")
        except (TypeError, ValueError):
            # Fallback if result isn't a number for some reason
            print(f"{num1} {symbol} {num2} = {result}")


if __name__ == "__main__":
    calculator()

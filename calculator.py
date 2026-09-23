"""Simple calculator with input validation, including division-by-zero handling."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    """Divide a by b. Raises ValueError on division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def calculate(operation, a, b):
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }
    if operation not in operations:
        raise ValueError(f"Unsupported operation: {operation}")
    return operations[operation](a, b)


if __name__ == "__main__":
    assert divide(10, 2) == 5
    try:
        divide(1, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"
    else:
        raise AssertionError("divide(1, 0) should raise ValueError")
    print("All checks passed, including division-by-zero handling.")

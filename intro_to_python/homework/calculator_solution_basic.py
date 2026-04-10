"""
Task: Build a calculator that remembers results and supports multiple operations.

Requirements:
1. Create a calculator that takes two numbers and an operation
2. Support operations: +, -, *, /, ** (power), // (floor division), % (modulo)
3. Store last 3 results in a dictionary with timestamps
4. Include "memory" feature: recall previous result using M1, M2, M3
5. Handle errors: division by zero, invalid operation

Example usage:
calc = create_calculator()
result = calculate(calc, 10, 3, "+")  # Returns 13
result = calculate(calc, 5, 2, "**")  # Returns 25
result = calculate(calc, "M1", 5, "*")  # Uses result 13, returns 65
"""

from datetime import datetime


def create_calculator():
    """
    Initialize calculator with empty history.
    Returns dict with 'history': {1: None, 2: None, 3: None}
    """
    return {
        "history": {1: None, 2: None, 3: None},
        "last_operation_time": None
    }


def calculate(calc, a, b, operation):
    """
    Perform calculation and update history.

    Args:
        calc: calculator dictionary
        a: number or "M1"/"M2"/"M3" to recall memory
        b: number or "M1"/"M2"/"M3" to recall memory
        operation: string "+", "-", "*", "/", "**", "//", "%"

    Returns:
        result or error message string

    Updates calculator history (shifts old results: 3→2, 2→1, 1→new)
    """
    # Step 1: Resolve memory references (M1, M2, M3)
    # Step 2: Validate operation
    # Step 3: Perform calculation with error handling
    # Step 4: Update history (shift 2→3, 1→2, new→1)
    # Step 5: Return result

    # Resolve memory references
    history = calc["history"]
    if str(a).startswith("M"):
        mem_slot = int(a[1])
        a = history.get(mem_slot)
        if a is None:
            return "Error: Memory empty"

    if isinstance(b, str) and b.startswith("M"):
        mem_slot = int(b[1])
        b = history.get(mem_slot)
        if b is None:
            return "Error: Memory empty"

    # Validate operation
    if operation not in {"+", "-", "*", "/", "**", "//", "%"}:
        return "Error: Invalid operation"

    # Calculate
    result = None
    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    elif operation == "/":
        if b != 0:
            result = a / b
        else:
            result = "Error: Division by zero"
    elif operation == "**":
        result = a ** b
    elif operation == "//":
        result = a // b if b != 0 else "Error: Division by zero"
    elif operation == "%":
        result = a % b if b != 0 else "Error: Division by zero"

    if str(result).startswith("Error"):
        return result

    # Update history (shift: 2->3, 1->2, new->1)
    new_calc = {
        "history": {
            1: result,
            2: history[1],
            3: history[2]
        },
        "last_operation_time": datetime.now().today()
    }
    calc.update(new_calc)  # In real solution, return new calc

    return result


def get_history(calc):
    """Return formatted string showing calculation history."""
    return str(calc.get("history"))


def clear_history(calc):
    """Reset history to empty. Return new calculator dict."""
    calc.update({"history": {1: None, 2: None, 3: None}})


# Test cases
calc = create_calculator()

# Basic operations
print(calculate(calc, 10, 3, "+"))      # 13
# Current history  {1: 13, 2: None, 3: None}

print(calculate(calc, 5, 2, "**"))      # 25
# Current history  {1: 25, 2: 13, 3: None}

print(calculate(calc, 20, 4, "/"))      # 5.0
# Current history  {1: 5.0, 2: 25, 3: 13}

# Memory operations
print(calculate(calc, "M1", 2, "*"))    # 10.0 (5.0 * 2)
# Current history  {1: 10.0, 2: 5.0, 3: 25}

print(calculate(calc, "M1", "M3", "+")) # 35.0 (10.0 + 25)

# Error handling
print(calculate(calc, 10, 0, "/"))      # "Error: Division by zero"
print(calculate(calc, 10, 5, "unknown")) # "Error: Invalid operation"

# Check history
print(get_history(calc))  # {1: 35.0, 2: 10.0, 3: 5.0}
print(calc.get("last_operation_time"))
from datetime import datetime


def create_calculator():
    """
    Initialize calculator with empty history.
    Returns dict with 'history': [] (unlimited storage)
    """
    return {
        "history": [],  # List stores infinite results with timestamps
        "last_operation_time": None
    }


def calculate(calc, a, b, operation):
    """
    Perform calculation and update history.

    Args:
        calc: calculator dictionary
        a: number or "M1"/"M2"/"M3"/... to recall memory
        b: number or "M1"/"M2"/"M3"/... to recall memory
        operation: string "+", "-", "*", "/", "**", "//", "%"

    Returns:
        result or error message string

    Updates calculator history (appends new result with timestamp)
    """
    history = calc["history"]

    # Helper function to resolve memory references (M1, M2, M3, ...)
    def resolve_memory(value):
        if isinstance(value, str) and value.startswith("M"):
            try:
                mem_slot = int(value[1:])  # Supports M1, M12, M123, etc.
                if mem_slot < 1:
                    return "Error: Invalid memory reference"
                if mem_slot > len(history):
                    return "Error: Memory empty"
                # M1 = most recent (index -1), M2 = second recent (index -2), etc.
                return history[-mem_slot]["result"]
            except ValueError:
                return "Error: Invalid memory reference"
        return value

    # Resolve memory references
    a = resolve_memory(a)
    if isinstance(a, str) and a.startswith("Error"):
        return a

    b = resolve_memory(b)
    if isinstance(b, str) and b.startswith("Error"):
        return b

    # Validate operation
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y if y != 0 else "Error: Division by zero",
        "**": lambda x, y: x ** y,
        "//": lambda x, y: x // y if y != 0 else "Error: Division by zero",
        "%": lambda x, y: x % y if y != 0 else "Error: Division by zero"
    }

    if operation not in operations:
        return "Error: Invalid operation"

    # Calculate
    result = operations[operation](a, b)
    if isinstance(result, str) and result.startswith("Error"):
        return result

    # Update history - append new result with timestamp (infinite storage)
    history.append({
        "result": result,
        "timestamp": datetime.now(),
        "operation": f"{a} {operation} {b}"
    })
    calc["last_operation_time"] = history[-1]["timestamp"]

    return result


def get_history(calc, limit=None):
    """
    Return formatted string showing calculation history.

    Args:
        calc: calculator dictionary
        limit: optional int to show only last N results
    """
    history = calc.get("history", [])
    if not history:
        return "No calculation history"

    # Show most recent first (M1, M2, M3...)
    lines = []
    display_items = history[-limit:] if limit else history

    for i, entry in enumerate(reversed(display_items), 1):
        actual_index = len(history) - i + 1
        lines.append(
            f"M{i} (calc #{actual_index}): {entry['result']} "
            f"[{entry['operation']}] @ {entry['timestamp'].strftime('%H:%M:%S')}"
        )

    return "\n".join(lines)


def clear_history(calc):
    """Reset history to empty. Return new calculator dict."""
    calc["history"] = []
    return calc



# Test cases
calc = create_calculator()

# Basic operations
print("=== Basic Operations ===")
print(calculate(calc, 10, 3, "+"))  # 13
print(calculate(calc, 5, 2, "**"))  # 25
print(calculate(calc, 20, 4, "/"))  # 5.0

# Memory operations - now supports infinite memory!
print("\n=== Memory Operations ===")
print(calculate(calc, "M1", 2, "*"))  # 10.0 (5.0 * 2)
print(calculate(calc, "M1", "M3", "+"))  # 35.0 (10.0 + 25)
print(calculate(calc, 100, 50, "-"))  # 50

# Access older memories (M4, M5, etc. - now possible!)
print(get_history(calc))
print(calculate(calc, "M4", 10, "+"))  # 15 (5 + 10, from 4 calculations ago)
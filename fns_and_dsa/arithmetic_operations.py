def perform_operation(num1: float, num2: float, operation: str) -> float:
    """
    Perform basic arithmetic operations on two numbers.
    
    Args:
        num1: First number
        num2: Second number
        operation: One of 'add', 'subtract', 'multiply', or 'divide'
    
    Returns:
        Result of the arithmetic operation, or None for division by zero
    """
    operation = operation.lower()
    
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return None  # This will be handled in main.py
        return num1 / num2
    else:
        return None  # For invalid operations

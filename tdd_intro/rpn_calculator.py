def evaluate(expression: str) -> float:
    expression = expression.split(" ")
    nums = [i for i in expression if i.isdigit()]
    operands = len(expression) - len(nums)
    if operands == 0 and len(nums) == 1:
        return int(nums[0])
    elif operands != len(nums) - 1:
        raise ValueError("Incorrect number of operands")
    pos = 0
    while len(expression) > 1:
        if expression[pos].isdigit():
            pos += 1
        else:
            a = float(expression[pos - 2])
            b = float(expression[pos - 1])
            if expression[pos] == "+":
                value = a + b
            elif expression[pos] == "-":
                value = a - b
            elif expression[pos] == "*":
                value = a * b
            elif expression[pos] == "/":
                value = a / b
                if b == 0:
                    raise ZeroDivisionError("Division by zero")
            else:
                raise ValueError("Incorrect character")
            temp = expression[:pos - 2]
            temp.append(value)
            temp.extend(expression[pos + 1:])
            expression = temp
            pos -= 1
    try:
        num = int(expression[0])
        if num != float(expression[0]):
            num = float(expression[0])
    except ValueError:
        num = float(expression[0])
    return num

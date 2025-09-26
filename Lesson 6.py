def solving_equation(equation):
    stack = []
    items = equation.split()

    for item in items:
        if item.isdigit() or (item.startswith('-') and item[1:].isdigit()):
            stack.append(int(item))
        else:
            b = stack.pop()
            a = stack.pop()
            if item == '+':
                 stack.append(a + b)
            elif item == '-':
                 stack.append(a - b)
            elif item == '*':
                 stack.append(a * b)
            elif item == '/':
                stack.append(int(a / b))

    return stack.pop()

print(solving_equation("16 1 - 5 / 2 *"))
print(solving_equation("25 5 / 3 * 4 +"))
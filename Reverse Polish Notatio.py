def evaluate_rpn(expression):

    stack = []


    tokens = expression.split()


    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            op2 = stack.pop()
            op1 = stack.pop()

            if token == '+':
                result = op1 + op2
            elif token == '-':
                result = op1 - op2
            elif token == '*':
                result = op1 * op2
            elif token == '/':
                result = op1 / op2

            stack.append(result)

    return stack.pop()



rpn_expression = "3 4 2 * +"
result = evaluate_rpn(rpn_expression)
print(result)

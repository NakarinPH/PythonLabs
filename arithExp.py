"""
File: arithExp.py
Author: Nakarin Philangam
A program for evaluating arithmetic expressions.
"""

from liststack import ListStack


def infix_to_postfix(infix_exp):
    """ Converts infix expression to postfix expression.
    Return postfix expression.
    Operands/operators are separated by spaces in expressions."""
    postfix_expression_stk = []
    stk = ListStack()
    exOrder = {'+': 1, '-': 1, '*': 2, '/': 2}

    for i in infix_exp.split():
        if i == '(':
            stk.push(i)
        elif i == ')':
            while len(stk) != 0 and stk.peek() != '(':
                postfix_expression_stk.append(stk.pop())
            if len(stk) == 0:
                return "Invalid Expression"
            else:
                stk.pop()
        elif i.isdigit() or i.isalpha():
            postfix_expression_stk.append(i)
        elif i in "+-*/":
            while len(stk) != 0 and (stk.peek() != '(') and (exOrder[i] <= exOrder[stk.peek()]):
                postfix_expression_stk.append(stk.pop())
            stk.push(i)
    while len(stk) != 0:
        postfix_expression_stk.append(stk.pop())
    return " ".join(postfix_expression_stk)


def main():
    infix = "4 + 5 * 6 - 3"
    postfix = infix_to_postfix(infix)
    print("Infix expression:", infix)
    print("postfix expression:", postfix)
    print()

    infix = "( 4 + 5 ) * ( 6 - 3 )"
    postfix = infix_to_postfix(infix)
    print("Infix expression:", infix)
    print("postfix expression:", postfix)


if __name__ == "__main__":
    main()

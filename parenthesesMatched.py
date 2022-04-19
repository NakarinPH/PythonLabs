"""Parentheses are used in mathematical expressions to denote modifications to normal order of operations.
They must be used in pairs and can be nested inside another pair. For example, parentheses in this expression ((5-2)*(3+6))*4 are matched properly,
while parentheses in this expression ((2*(3+6)+4)*5 are not.

Develop an algorithm for a function parenthesesMatched, which tests whether parentheses in a mathematical expression are matched properly.
This function has a parameter oper_list, which is a list that holds the operands and operators of a mathematical expression. For example,
the oper_list for the expression ((5-2)*(3+6))*4 is ['(', '(', '5', '-', '2', ')', '*', '(', '3', '+', '6', ')', ')', '*', '4'].
This function returns True if the parentheses are matched properly, and False otherwise. [Hint: Consider using a stack]
"""
def parenthesesMatched(oper_list):
    # returns True if the parentheses are matched properly, and False otherwise.
    stk = []
    for operands in oper_list:
        if operands == '(':
            stk.append(operands)
        elif operands == ')':
            stk.pop(-1)
    if len(stk) == 0:
        print('Parenthesis matched')
    else:
        print('Parenthesis NOT matched')

def parenthesesMatched1(oper_list):
    stk = []
    for operands in oper_list:
        if operands == '(':
            stk.append(operands)
        elif operands == ')':
            if len(stk) == 0:
                print("Not matched")
            else:
                stk.pop()
    if len(stk) == 0:
        print("Matched")
    else:
        print("Not matched")


oper_list = ['(', '(', '5', '-', '2', ')', '*', '(', '3', '+', '6', ')', ')', '*', '4']
parenthesesMatched(oper_list)
parenthesesMatched1(oper_list)

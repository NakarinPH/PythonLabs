
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


oper_list = ['(', '(', '5', '-', '2', ')', '*', '(', '3', '+', '6', ')', ')', '*', '4']
parenthesesMatched(oper_list)

import Constants as con

def func(a, b, operation):
    if operation == con.Addition:
        return a+b
    if operation == con.Subtraction:
        return a-b
    if operation == con.Multiplication:
        return a*b
    if operation == con.Division:
        return a/b
    else:
        return "wrong operation code"
    # Use a breakpoint in the code line below to debug your script.
    # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
a = input()
b = input()
op = input()
print(func(a, b, op))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

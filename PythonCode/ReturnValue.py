def Return_value():
    return "have value"

def no_Return_Value():
    return

a = Return_value()
b = no_Return_Value()

print(a)#有返回值“have value”

print(b)#无返回值，默认返回None
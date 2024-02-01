def calculator(func):
    def idk(expression):
        try:
            result = func(expression)
            return result
        except Exception:
            print(f"Но Но Но на нуль ділити неможна")
            return None

    return idk

@calculator
def calculate(expression):
    a = int(input("число 1"))
    b = int(input("число 2"))
    return eval(expression)


result = calculate("a / b")
print(f"Осьо така відповідь: {result}")
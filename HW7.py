def calculator(Funnition):
    def XYZ(expression):
        try:
            result = Funnition(expression)
            return result
        except Exception:
            print(f"Но Но Но на нуль ділити неможна")
            return None

    return XYZ

@calculator
def calculate(expression):
    a = int(input("число 1"))
    b = int(input("число 2"))
    return eval(expression)


result = calculate("a/b")
print(f"Осьо така відповідь: {result}")

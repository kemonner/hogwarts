class Calc:

    def add(self, a: int, b: int):
        print("calc在此")
        return a + b

    def add1(self, a: int, b: int):
        print("calc在此")
        return a + b

    def sub(self, a: int, b: int):
        print("calc在此")
        return a - b

    def div(self, a: int, b: int):
        print("calc在此")
        return a / b


calc = Calc()
# test_add(1, 2)
calc.div(2, 2)
calc.add(2, 2)
print("calc在此")

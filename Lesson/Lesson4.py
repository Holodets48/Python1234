class Gr:
    height = 170
    satiety = 100
    age = 60

class Pr(Gr):
    age = 50
    def __init__(self):
        print(f"height - {self.height}")
        print(f"satiety - {self.satiety}")
        print(f"age - {self.age}")
class Cl(Pr):
    height = 50
    age = 5
    def __init__(self):
        print(f"height - {self.height}")
        print(f"satiety - {self.satiety}")
        print(f"age - {self.age}")

nick = Cl()
print("#"*50)

class H:
    def __init__(self):
        print("Hello")

class HWW(H):
    def __init__(self):
        super().__init__()
        print("World")

abobus = HWW()
print("#"*50)

class CL1:
    var = 20
    def __init__(self):
        self.var = 10

class CL2(CL1):
    def __init__(self):
        print(self.var)
        super().__init__()
        print(self.var)

c = CL2()
print("#"*50)
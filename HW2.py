class Dog:
    def __init__(self):
        self.energy = 50
        self.happy = 50

    def play(self):
        self.energy -= 5
        self.happy += 10

    def food(self):
        self.happy += 5

    def walk(self):
        self.energy -= 5
        self.happy += 5

    def sleep(self):
        self.energy += 10
        self.happy -= 10

    def Pinfo(self):
        print(f"Energy - {self.energy}")
        print(f"Happy - {self.happy}")

Frenk = Dog()
Frenk.sleep()
Frenk.food()
Frenk.walk()
Frenk.sleep()
Frenk.food()
Frenk.walk()
Frenk.play()
Frenk.sleep()

Frenk.Pinfo()

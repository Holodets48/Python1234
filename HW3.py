class Student:
    def __init__(self, name):
        self.name = name
        self.grade = 0
        self.smart = 0

    def study(self):
        print(f"{self.name} Вчиться на ВЕЛИКОМУ КУРСІ ЯК СТАТИ ДУРНЕМ")
        self.smart += 10

    def take_exam(self):
        print(f"{self.name} Заповнює ненужні бумаги")
        self.grade += 10
    def printInfo(self):
        print(f"Геніальність - {self.smart}")
        print(f"Оцінка Геніальності - {self.grade}")
class Teacher:
    def __init__(self, name):
        self.name = name
        self.payment = 0

    def teach(self):
        print(f"{self.name} Вчить геніїв як правильно жити")
        self.payment += 10


    def evaluate(self):
        print(f"{self.name} Оцінює генія")
        self.payment += 5
    def printPay(self):
        print(f"Великі гроші(в копійках) - {self.payment}")

St = Student(name="Dima")
fizicka = Teacher(name="Olena Ikeniiwna")
St.take_exam()
St.study()
St.printInfo()
fizicka.teach()
fizicka.evaluate()
fizicka.printPay()
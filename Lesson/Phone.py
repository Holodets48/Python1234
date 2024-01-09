class mobile_phone:
    def __init__(self, display, model, brand):
        self.brand = brand
        self.model = model
        self.display = display
    def CD(self, connect_link):
        self.cd = connect_link

p1 = mobile_phone(6.2,"Samsung","S23")

p2 = mobile_phone(5.5,"Apple","11")

print(p1.cd.display)
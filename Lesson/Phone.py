class mobile_phone:
    def __init__(self, display, model, brand):
        self.brand = brand
        self.model = model
        self.display = display

class samsung(mobile_phone):
    def __init__(self):
        self.brand = samsung
        self.model = Galaxy_A34
        self.display = 6.6

class apple(mobile_phone):
    def __init__(self):
        self.brand = apple
        self.model = Aphone_11
        self.display = 6.1

class xiomi(mobile_phone):
    def __init__(self):
        self.brand = xiomi
        self.model = Xiomi_9
        self.display = 6.5

class huawei(mobile_phone):
    def __init__(self):
        self.brand = huawei
        self.model = Huawei_P30_Lite
        self.display = 6.1

print(xiomi.display)
class bluetoothdevice:
    def __init__(self, brand, model, maxVolume, bass):
        self.brand = brand
        self.model = model
        self.maxVolume = maxVolume
        self.bass = bass
    def conect(self, cOnnectLink):
        self.BTdevice1 = cOnnectLink

ColonkaD1 = bluetoothdevice("JBL","partybox310",1984,"yes")

ColonkaD2 = bluetoothdevice("JBL","Charge4",1488,"no")

ColonkaD1.conect(ColonkaD2)
print(ColonkaD1.BTdevice1.maxVolume)

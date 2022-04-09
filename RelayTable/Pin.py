class Pin:
    count = -1
    def __init__(self, name=""):
        Pin.count +=1
        self.number = Pin.count
        if name == "":
            self.name = f'Net{self.number}'
        else:
            self.name = name
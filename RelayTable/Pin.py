from Net import Net
class Pin:
    count = -1
    def __init__(self, name=""):
        Pin.count +=1
        self.number = Pin.count
        self.Net = Net("defult")
        if name == "":
            self.name = f'Net{self.number}'
        else:
            self.name = name

import Pin
class Component:
    def __init__(self) -> None:
        self.pindict = dict()
        self.name = str()
    def printallpins(self):
        print(p for p in self.pindict)

class group:
    def __init__(self) -> None:
        self.list = list()
    def connect(self,pin:str,net):
        for comp in self.list:
            Pin.connect(comp.pindict[pin],net)
    def name(self,name:str):
        for comp in self.list:
            comp.name = name

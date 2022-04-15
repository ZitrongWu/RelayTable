from Pin import Pin
class Component:
    def __init__(self) -> None:
        self.pinlist = list()
    def printallpins(self):
        print(p for p in self.pinlist)


class Net:
    count = -1
    def __init__(self,name = "") -> None:
        Net.count +=1
        self.number = Net.count
        self.pins = list()
        if name == "":
            self.name = f'K{self.number}'
        else:
            self.name = name    
    def __repr__(self):
        return self.name


class Pin:
    count = -1
    def __init__(self, name=""):
        Pin.count +=1
        self.number = Pin.count
        if name == "":
            self.name = f'Pin{self.number}'
        else:
            self.name = name
        self.net = Net(f'NetP{self.name}')
        self.component = None
    def __repr__(self):
        # return f'Pin{self.number}_{self.name}_{self.net.name}'
        return f'Pin{self.number}_{self.name}'
    def __str__(self) -> str:
        return f'{self.name}'

def connect(pin:Pin,net:Net):
    pin.net = net
    net.pins.append(pin)
    



# def main():
#     pin1 = Pin()
#     pin2 = Pin()
#     connect(pin1,pin2,"newnet")
#     print(pin1.net.pins)
   
# if __name__ == '__main__':
#     main()


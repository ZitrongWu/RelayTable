
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
    def __repr__(self):
        return f'Pin{self.number}_{self.name}_{self.net.name}'

def connect(pinself:Pin,pin:Pin,netname = ""):
    if netname != "":
        pinself.net.name = netname
    pin.net = pinself.net
    pinself.net.pins.append(pinself)
    pinself.net.pins.append(pin)
    



# def main():
#     pin1 = Pin()
#     pin2 = Pin()
#     connect(pin1,pin2,"newnet")
#     print(pin1.net.pins)
   
# if __name__ == '__main__':
#     main()


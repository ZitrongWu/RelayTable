from Net import Net
class Pin:
    count = -1
    def __init__(self, name=""):
        Pin.count +=1
        self.number = Pin.count
        if name == "":
            self.name = f'Net{self.number}'
        else:
            self.name = name
    def __str__(self):
        return f'Pin{self.number},name:{self.name},net:{self.net.name}'
def connect(pinself:Pin,pin:Pin,netname = ""):
    if netname == "":
        pinself.net = Net() 
    else:
        pinself.net = Net(netname)
    pinself.net.pins.append(pinself)
    pinself.net.pins.append(pin)
    pin.net = pinself.net

def main():
    pin1 = Pin("pin1")
    pin2 = Pin("pin2")
    connect(pin1,pin2,"new net")
    print("Test")
    print(pin1)
    print(pin2)
    print(pin1.net.pins)
   
if __name__ == '__main__':
    main()


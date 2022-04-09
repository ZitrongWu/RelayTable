from Pin import Pin
class Net:
    count = -1
    def __init__(self,name = "") -> None:
        Net.count +=1
        self.number = Net.count
        if name == "":
            self.name = f'K{self.number}'
        else:
            self.name = name    
        self.pins = list()    
    def connect(self,pin:Pin):
        self.pins.append(pin)


def main():
    pin1 = Pin("Pin1")
    pin2 = Pin("Pin2")
    net = Net("defult")
    net.connect(pin1)
    net.connect(pin2)
    print(net.pins[0].name)
    print(net.pins[1].name)

if __name__ == "__main__":
    main()

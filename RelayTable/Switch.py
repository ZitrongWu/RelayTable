import RelayTable.Net as Net
import RelayTable.Relay as Relay

class Switch:
    count = -1
    def __init__(self, name=""):
        Switch.count +=1
        self.number = Switch.count
        if name == "":
            self.name = f'Switchnet{self.number}'
        else:
            self.name = name
        self.const = Net(f'Switchnet{self.number}C')
        self.relays = []
    def addto(self,net:Net,rel:Relay):
        self.relay = []
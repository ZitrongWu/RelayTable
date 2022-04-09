import RelayTable.Pin as Pin
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
        self.const = Pin(f'Switchnet{self.number}C')
        self.relays = []
    def addto(self,net:Pin,rel:Relay):
        self.relay = []
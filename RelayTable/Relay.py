import RelayTable.Pin as Pin
class Relay:
    "A Relay class"
    count = -1
    def __init__(self, name=""):
        Relay.count +=1
        self.number = Relay.count
        if name == "":
            self.name = f'K{self.number}'
        else:
            self.name = name
        self.inline = Pin(self.name + 'I')
        self.copen = Pin(self.name + 'CO')
        self.cclose = Pin(self.name + 'CC')
    def connect(self,inl:Pin, copen:Pin, cc:Pin):
        self.inline = inl
        self.copen = copen
        self.cclose = cc
    


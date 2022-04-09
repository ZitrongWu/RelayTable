import RelayTable.Net as Net
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
        self.inline = Net(self.name + 'I')
        self.copen = Net(self.name + 'CO')
        self.cclose = Net(self.name + 'CC')
    def connect(self,inl:Net, copen:Net, cc:Net):
        self.inline = inl
        self.copen = copen
        self.cclose = cc
    


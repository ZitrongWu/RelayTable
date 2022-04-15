from Pin import Pin,Net,connect
from Component import Component
class key(Component):
    "A Relay class"
    count = -1
    def __init__(self, name=""):
        super().__init__()
        key.count +=1
        self.number = key.count
        if name == "":
            self.name = f'K{self.number}'
        else:
            self.name = name
        self.inline = Pin(self.name + 'I')
        self.inline.component = self
        self.pindict['I']=self.inline

        self.copen = Pin(self.name + 'CO')
        self.copen.component = self
        self.pindict['CO']=self.copen

        self.cclose = Pin(self.name + 'CC')
        self.cclose.component = self
        self.pindict['CC']=self.cclose

        self.controlA = Pin(self.name + 'controlA')
        self.controlA.component = self
        self.pindict['controlA']=self.controlA

        self.controlB = Pin(self.name + 'controlB')
        self.controlB.component = self
        self.pindict['controlB']=self.controlB               

    def __repr__(self):
        # return f'{self.inline.net}-K{self.number}-{self.copen.net}-{self.cclose.net}'
        return self.name
    def __str__(self) -> str:
        return self.name




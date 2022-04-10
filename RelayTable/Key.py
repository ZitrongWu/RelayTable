from Pin import Pin,Net,connect
class key:
    "A Relay class"
    count = -1
    def __init__(self, name=""):
        key.count +=1
        self.number = key.count
        if name == "":
            self.name = f'K{self.number}'
        else:
            self.name = name
        self.inline = Pin(self.name + 'I')
        self.copen = Pin(self.name + 'CO')
        self.cclose = Pin(self.name + 'CC')


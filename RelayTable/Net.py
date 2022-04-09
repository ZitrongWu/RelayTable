class Net:
    count = -1
    def __init__(self, name=""):
        Net.count +=1
        self.number = Net.count
        if name == "":
            self.name = f'Net{self.number}'
        else:
            self.name = name        
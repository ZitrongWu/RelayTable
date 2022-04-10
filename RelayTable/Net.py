class Net:
    count = -1
    def __init__(self,name = "") -> None:
        Net.count +=1
        self.number = Net.count
        if name == "":
            self.name = f'K{self.number}'
        else:
            self.name = name    



from Key import key
from Pin import Pin,Net,connect
class Switch:
    count = -1
    def __init__(self,name = "",) -> None:
        Switch.count += 1
        if name == "":
            self.name = f'SW{Switch.count}'
        else:
            self.name = name
        self.keylist = list()
    def __repr__(self) -> str:
        return f'Source net:{self.source}\r\nSwitch to {self.target}\r\nSolution:{self.keylist}'
    def __resolve_kernle__(self,sourcenet:Net,targetnet:list):
        if len(targetnet) == 0:
            return
        if len(targetnet) == 1:
            newkey = key()
            self.keylist.append(newkey)
            connect(newkey.copen,targetnet[0])        
            connect(sourcenet,newkey.inline)
            return
        if len(targetnet) == 2:
            newkey = key()
            self.keylist.append(newkey)
            connect(newkey.copen,targetnet[0]) 
            connect(newkey.cclose,targetnet[1])       
            connect(newkey.inline,self.source)
            return       
        n = 0
        keyinlinlist = list()
        while n+1<=len(targetnet)-1:
            newkey = key()
            self.keylist.append(newkey)
            keyinlinlist.append(newkey.inline.net)
            connect(newkey.copen,targetnet[n])
            connect(newkey.cclose,targetnet[n+1])
            n+=2
        self. __resolve_kernle__(sourcenet,keyinlinlist+targetnet[n:])
        return
    def resolve(self,source:Net,target:list,):
        self.source = source
        self.target = target
        self.__resolve_kernle__(self.source,self.target)
    def resolve(self,source:Pin,target:list,):
        self.source = source.net
        self.target = [t.net for t in target]     
        self.__resolve_kernle__(self.source,self.target)
    def find(slef,pinA:Pin,pinb:Pin)->list:
        pass

# def main():
#     pinA = Pin()
#     pin1 = Pin()
#     pin2 = Pin()
#     pin3 = Pin()
#     pin4 = Pin()
#     pin5 = Pin()

#     resolve(pinA,[pin1,pin2,pin3,pin4,pin5])
#     print(pinA.net,pin1.net,pin2.net,pin3.net,pin4.net,pin5.net)    
#     print(keylist)
   
# if __name__ == '__main__':
#     main()
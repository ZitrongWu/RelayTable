from Pin import Net
import Switch as sw
from Key import key
import pandas as pd
import Component as cm
class Testplan:
    count = -1
    def __init__(self,fileNameStr:str) -> None:
        Testplan.count+=1
        self.number = Testplan.count
        self.__filedir__=fileNameStr
    def read(self):
        self.__df__ = pd.read_excel(self.__filedir__,engine="openpyxl",sheet_name = 'Sheet1')
        self.pindict = dict()
        self.switchlist = list()
        self.keylist = list()
        for p,s in self.__df__.iloc[:,1:].items():
            self.sourcepin = list()
            pin = sw.Pin(s.name)
            for source in s.to_numpy():
                if source not in self.pindict:
                    self.pindict[source] = sw.Pin(source) 
                if self.pindict[source] not in self.sourcepin:
                    self.sourcepin.append(self.pindict[source])

            pinsw=sw.Switch(pin)
            pinsw.resolve(pin,self.sourcepin)
            self.switchlist.append(pinsw)
            self.keylist+=pinsw.keylist
    def generatekeys(self):
        self.__df__["Relay On"]=""
        self.keyactionlist=list()
        for n in range(self.__df__.shape[0]):
            action = list()
            targetpin = self.__df__.iloc[n,1:-2].to_numpy()
            # print(targetpin)
            for i,t in enumerate(targetpin):
                action+=(self.switchlist[i].find(self.pindict[t].net))
                # print(networklist[i].target)

            self.__df__['Relay On'].iloc[n] = (",".join(str(k) for k in action))       

            self.keyactionlist.append(action)

    def __synccheck__(self,keyA:key,keyB:key)->bool:
        for kl in self.keyactionlist:
            if keyA in kl and keyB not in kl:
                return False
            if keyB in kl and keyA not in kl:
                return False
        return True

    def find_sync_keys(self):
        self.keygrouplist = list()
        keylist = self.keylist
        
        while keylist:
            group = cm.group()
            ka = keylist[0]
            group.list.append(ka)
            keylist.pop(0)
            for n,kb in enumerate(keylist):
                if self.__synccheck__(ka,kb):
                    group.list.append(kb)
                    keylist.pop(n)

            self.keygrouplist.append(group)

    def connet_keygroup(self):
        for n,g in enumerate(self.keygrouplist):
            # print(g.list[0].pindict["controlA"])
            net = Net(f'cbit{n}')
            g.connect("controlA",net)
            # print(g.list,[k.pindict["controlA"].net for k in g.list])

        # self.__df2__ = pd.DataFrame(self.keylist)
        # print(self.__df2__)

    def write(self):
        with pd.ExcelWriter(self.__filedir__,engine='openpyxl',mode="a",if_sheet_exists='replace') as writer:
            self.__df__.to_excel(writer,sheet_name = "Sheet1",index=False)   
            self.__df2__.to_excel(writer,sheet_name = "Sheet2",index=False) 

    def __repr__(self) -> str:
        return str(self.__df__)


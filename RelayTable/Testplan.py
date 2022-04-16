from Pin import Net,Pin
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
        self.netdict = dict()
        self.switchlist = list()
        self.keylist = list()
        
        for p,s in self.__df__.iloc[:,1:-2].items():
            sourcepindict = dict()
            pin = Pin(s.name)
            for sourcename in s.to_numpy():
                if sourcename not in self.pindict:
                    # self.pindict[sourcename] = Pin(sourcename) 
                    self.creatpin(sourcename)

                sourcepindict[sourcename] = self.pindict[sourcename]
            #rewrit to creat switch
            pinsw=sw.Switch(pin)
            self.switchlist.append(pinsw)
            #end of rewrit to creat switch
            pinsw.resolve(pin,sourcepindict.values())
            

                
            self.keylist+=pinsw.keylist#rewrit to add keys
        
        self.creatpin("VCC")
        for k in self.keylist:
            k.pindict["controlB"].net = self.pindict["VCC"].net        
        

        print(self.pindict)
        print(self.netdict)

    def creatnet(self,name:str)->Net:
        net = Net(name)
        self.netdict[name] = net
        return net

    def creatpin(self,name:str)->Pin:
        pin = Pin(name)
        self.addpin(pin) 
        return pin

    def addpin(self,pin:Pin)->Pin:
        self.pindict[pin.name] = pin
        self.netdict[pin.net.name] = pin.net 
        return pin

    def generate_key_actions(self):
        self.__df__["Relay On"]=""
        self.keyactionlist=list()
        for n in range(self.__df__.shape[0]):
            action = list()
            targetpin = self.__df__.iloc[n,1:-2].to_numpy()
            # print(targetpin)
            for i,t in enumerate(targetpin):
                action+=(self.switchlist[i].find(self.pindict[t].net))
                # print(networklist[i].target)

            # self.__df__['Relay On'].iloc[n] = (",".join(str(k) for k in action))       

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
        
        # keylist = self.keylist
        __templist__ = list([1 for k in self.keylist])
        for n,ka in enumerate(self.keylist):
            if __templist__[n]:
                group = cm.group()
                # print(f'ka={ka}')
                group.list.append(ka)
                __templist__[n]=0
                for m,kb in enumerate(self.keylist[n+1:]):
                    if __templist__[m+n+1]:
                        # print(f'kb={kb}')
                        if self.__synccheck__(ka,kb):
                            group.list.append(kb)
                            __templist__[m+n+1]=0
                            

                # print(group.list)
                self.keygrouplist.append(group)
        

    def connet_keygroup(self):
        
        for n,g in enumerate(self.keygrouplist):
            # print(g.list[0].pindict["controlA"])
            # net = Net(f'cbit{n}')
            pin = self.creatpin(f'C{n}')
            g.connect("controlA",pin.net)
            # print(g.list,[k.pindict["controlA"].net for k in g.list])
        
        self.cbitactionlist = list()
        
        for action in self.keyactionlist:
            actioncbitdict = dict()
            for k in action:
                actioncbitdict[k.pindict["controlA"].net]=k.pindict["controlA"].net
            self.cbitactionlist.append(actioncbitdict.values())
        self.__savetodf__()
        
    def __savetodf__(self):
        if not self.keylist:
            return
        d = {"Relays":self.keylist}
        for pinnam in self.keylist[0].pindict:
            # print(pinnam)
            d[pinnam] = [k.pindict[pinnam].net for k in self.keylist]
        # print(d)
        self.__pintable__ = pd.DataFrame(d)
        # print(self.__pintable__)
        for n,cbit in enumerate(self.cbitactionlist):
            self.__df__['Relay On'].iloc[n] = (",".join(str(c) for c in cbit))
        print(self.__df__)
    def write(self):
        with pd.ExcelWriter(self.__filedir__,engine='openpyxl',mode="a",if_sheet_exists='replace') as writer:
            self.__df__.to_excel(writer,sheet_name = "Sheet1",index=False)   
            self.__pintable__.to_excel(writer,sheet_name = "Sheet2",index=False) 

    def __repr__(self) -> str:
        return str(self.__df__)


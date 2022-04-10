from Key import key
from Pin import Pin,Net,connect
keylist = list()
def resolve(pinA:Pin,pinlist:list):
    if len(pinlist) == 0:
        return
    if len(pinlist) == 1:
        newkey = key()
        keylist.append(newkey)
        connect(newkey.copen,pinlist[0])        
        connect(pinA,newkey.inline)
        return
    if len(pinlist) == 2:
        newkey = key()
        keylist.append(newkey)
        connect(newkey.copen,pinlist[0]) 
        connect(newkey.cclose,pinlist[1])       
        connect(pinA,newkey.inline)
        return       
    n = 0
    keyinlinlist = list()
    while n+1<=len(pinlist)-1:
        newkey = key()
        keylist.append(newkey)
        keyinlinlist.append(newkey.inline)
        connect(newkey.copen,pinlist[n])
        connect(newkey.cclose,pinlist[n+1])
        n+=2
    resolve(pinA,keyinlinlist+pinlist[n:])
    return

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
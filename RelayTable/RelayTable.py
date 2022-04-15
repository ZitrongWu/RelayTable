import pandas as pd
import numpy as np
import argparse
import Switch as sw
import Testplan as tp

def main():

    parse = argparse.ArgumentParser(description="Generat relay table base on input excel file")
    parse.add_argument('inputfile',metavar='f',type=str,help='Read from excel file')
    args = parse.parse_args()
    plan=tp.Testplan(args.inputfile)
    plan.read()
    plan.generatekeys()
    print(plan)
    plan.find_sync_keys()
    print(plan.keygrouplist)
    # # read data frome excel store in table
    # fileNameStr = args.inputfile
    # Test_plan = pd.read_excel(fileNameStr,engine="openpyxl",sheet_name = 'Sheet1')
    # pindict = dict()
    # networklist = list()
    # for p,s in Test_plan.iloc[:,1:].items():
    #     sourcepin = list()
    #     pin = sw.Pin(s.name)
    #     for source in s.to_numpy():
    #         if source not in pindict:
    #             pindict[source] = sw.Pin(source) 
    #         if pindict[source] not in sourcepin:
    #             sourcepin.append(pindict[source])

    #     network=sw.Switch(pin)
    #     network.resolve(pin,sourcepin)
    #     networklist.append(network)
    #     # print(network)

    # Test_plan["Relay On"]=""
    
    # for n in range(Test_plan.shape[0]):
    #     action = list()
    #     targetpin = Test_plan.iloc[n,1:-2].to_numpy()
    #     print(targetpin)
    #     for i,t in enumerate(targetpin):
    #         action+=(networklist[i].find(pindict[t].net))
    #         # print(networklist[i].target)

    #     Test_plan['Relay On'].iloc[n] = (",".join(str(k) for k in action))

    # print(Test_plan)
    
    #write back to excel

    # with pd.ExcelWriter(fileNameStr,engine='openpyxl',mode="a",if_sheet_exists='replace') as writer:
    #     Test_plan.to_excel(writer,sheet_name = "Sheet1",index=False)





if __name__ == "__main__":
    main()






import pandas as pd
import numpy as np
import Switch as sw


def main():

    # read data frome excel store in table
    fileNameStr = "RelayTable/RelayTable.xlsx"
    Test_plan = pd.read_excel(fileNameStr,engine="openpyxl",sheet_name = 'Sheet1')
    pindict = dict()
    networklist = list()
    for p,s in Test_plan.iloc[:,1:].items():
        sourcepin = list()
        pin = sw.Pin(s.name)
        for source in s.to_numpy():
            if source not in pindict:
                pindict[source] = sw.Pin(source) 
            if pindict[source] not in sourcepin:
                sourcepin.append(pindict[source])

        network=sw.Switch(pin)
        network.resolve(pin,sourcepin)
        networklist.append(network)
        # print(network)

    
    for n in range(Test_plan.shape[0]):
        action = list()
        targetpin = Test_plan.iloc[n,1:].to_numpy()
        print(targetpin)
        for i,t in enumerate(targetpin):
            action+=(networklist[i].find(pindict[t].net))
            # print(networklist[i].target)
        print(action)
    
    
    #write back to excel

    # with pd.ExcelWriter(fileNameStr,engine='openpyxl',mode="a",if_sheet_exists='replace') as writer:
    #     Test_plan.to_excel(writer,sheet_name = "Sheet3",index=False)

    #     relaytable_df.to_excel(writer,sheet_name = "Sheet2",index=False)





if __name__ == "__main__":
    main()






import pandas as pd
import numpy as np
import Switch as sw


def main():

    # read data frome excel store in table
    fileNameStr = "RelayTable/RelayTable.xlsx"
    Test_plan = pd.read_excel(fileNameStr,engine="openpyxl",sheet_name = 'Sheet1')
    netdict = dict()
    for p,s in Test_plan.iloc[:,1:].items():
        sourcepin = list()
        pin = sw.Pin(s.name)
        for source in s.to_numpy():
            if source not in netdict:
                netdict[source] = sw.Pin(source) 
            if netdict[source] not in sourcepin:
                sourcepin.append(netdict[source])
        # sourcepin.append(sw.Pin("FLOAT"))
        # print("Chip pin:",pin)
        # print("Switch to:",sourcepin)
        network=sw.Switch(pin)
        network.resolve(pin,sourcepin)
        # print("solusion:",network.keylist)
        print(network)
    #write back to excel

    # with pd.ExcelWriter(fileNameStr,engine='openpyxl',mode="a",if_sheet_exists='replace') as writer:
    #     Test_plan.to_excel(writer,sheet_name = "Sheet3",index=False)

    #     relaytable_df.to_excel(writer,sheet_name = "Sheet2",index=False)





if __name__ == "__main__":
    main()






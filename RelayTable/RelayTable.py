import pandas as pd


def main():



    fileNameStr = "RelayTable/RelayTable.xlsx"

    table = pd.read_excel(fileNameStr, 'Sheet1')

    relaytable_dic = {"Net_A":[],"Net_B":[]}

    head = table.keys()

    head = head[1:]


    relay_count = 0


    for r,row in enumerate(table.values[1:]):

        for c,model in enumerate(row[1:]):
            relaytable_dic["Net_A"].append(str(head[c]))
            relaytable_dic["Net_B"].append(str(model))

    relaytable_df = pd.DataFrame(relaytable_dic)
    relaytable_df.drop_duplicates(inplace=True)
    relaytable_df.index = range(relaytable_df.shape[0])
    add = pd.DataFrame(
        {
            "Relay":range(relaytable_df.shape[0])
        }
    )
    relaytable_df = pd.concat([relaytable_df,add],axis = 1)
    print(relaytable_df)

    with pd.ExcelWriter(fileNameStr) as writer:
        table.to_excel(writer,sheet_name = "Sheet1",index=False)
        relaytable_df.to_excel(writer,sheet_name = "Sheet2",index=False)
        





def hello(name):



    return f"Hello {name}!"





if __name__ == "__main__":
    main()




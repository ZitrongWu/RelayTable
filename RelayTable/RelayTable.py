import pandas as pd



def main():
    # read data frome excel store in table
    fileNameStr = "RelayTable/RelayTable.xlsx"
    table = pd.read_excel(fileNameStr,engine="openpyxl",sheet_name = 'Sheet1')

    # generate relay table based on items in table
    relaytable_dic = {"Net_A":[],"Net_B":[]}
    head = table.keys()
    head = head[1:]
    relay_count = 0
    for r,row in enumerate(table.values):
        for c,model in enumerate(row[1:]):
            model.strip(' ')          
            if model != "Float":
                relaytable_dic["Net_A"].append(str(head[c]))
                relaytable_dic["Net_B"].append(str(model))
    relaytable_df = pd.DataFrame(relaytable_dic)
    relaytable_df.drop_duplicates(inplace=True)# deduplicate the relay tabel
    relaytable_df.index = range(relaytable_df.shape[0])

    # generate a list of relays
    Relays_dic = {"Relay":[]}
    for r in range(relaytable_df.shape[0]):
        Relays_dic["Relay"].append(f'K{r}')
    Relays = pd.DataFrame(Relays_dic,index= range(relaytable_df.shape[0]))
    relaytable_df = pd.concat([relaytable_df,Relays],axis = 1)#connet the relay table with the relay list
    print("Relay table:")
    print(relaytable_df)



     
    # find out wich relay should be terned on for each test and record in the tabel
    REQ_relay = []
    for r,row in enumerate(table.values):
        REQ_relay_row = ""        
        for c,model in enumerate(row[1:]):
            if model != "Float":
                a = relaytable_df.loc[:,'Net_A'] == str(head[c])
                b = relaytable_df.loc[:,'Net_B'] == str(model)
                relay = relaytable_df.loc[a & b,"Relay"].values[0]
                REQ_relay_row = REQ_relay_row+","+str(relay)
        REQ_relay_row = REQ_relay_row.lstrip(",")
        REQ_relay.append(REQ_relay_row)
    REQ_relay_df = pd.DataFrame(REQ_relay,columns=["Relay"],index=range(table.shape[0]))
    table = pd.concat([table,REQ_relay_df],axis = 1)#connect two table
    print("Linked relay table:")
    print(table)    

    #write back to excel
    with pd.ExcelWriter(fileNameStr,engine='openpyxl',mode="a",if_sheet_exists='replace') as writer:
        table.to_excel(writer,sheet_name = "Sheet3",index=False)
        relaytable_df.to_excel(writer,sheet_name = "Sheet2",index=False)




if __name__ == "__main__":
    main()





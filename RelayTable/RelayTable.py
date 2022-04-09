import pandas as pd
import numpy as np



def main():

    # read data frome excel store in table

    fileNameStr = "RelayTable/RelayTable.xlsx"
    Test_plan = pd.read_excel(fileNameStr,engine="openpyxl",sheet_name = 'Sheet1')


    # generate relay table based on items in table

    relaytable_dic = {"Net_A":[],"Net_B":[]}

    head = Test_plan.keys()

    head = head[1:]

    for r,row in enumerate(Test_plan.values):


        for c,model in enumerate(row[1:]):

            model.strip(' ')          

            if model != "Float":

                relaytable_dic["Net_A"].append(str(head[c]))

                relaytable_dic["Net_B"].append(str(model))

    relaytable_df = pd.DataFrame(relaytable_dic)

    relaytable_df.drop_duplicates(inplace=True)# deduplicate the relay tabel

    relaytable_df.index = range(relaytable_df.shape[0])


    # generate a list of relays

    relay_count = 0

    contact_count = 0

    Relays_dic = {"Relay":[]}



   



    for i in range(relaytable_df.shape[0]):
        Relays_dic["Relay"].append(f'K{relay_count}')

        relay_count += 1

        # Relays_dic["Contact"].append(f'K{1}')
        


    Relays = pd.DataFrame(Relays_dic,index= range(relaytable_df.shape[0]))

    relaytable_df = pd.concat([relaytable_df,Relays],axis = 1)#connet the relay table with the relay list




    #compaire each column of test plan to find the syced net
    for i,(label,nets) in enumerate(Test_plan.iloc[:,1:].items()):
        for label_c,nets_c in Test_plan.iloc[:,i+2:].items():

            same = nets==nets_c
            diff = nets!=nets_c
            diff_net = nets.loc[diff]
            same_net = nets.loc[same]
            syc = pd.Series(np.ones(nets.shape),dtype=bool)
            for ind,val in diff_net.items():
                syc &= same_net != val

            syc_net = nets.loc[syc].drop_duplicates(inplace=False)
           
            
            if not syc_net.empty:
                for i,snet in syc_net.items():    
                    relaytable_df.loc[(relaytable_df.loc[:,"Net_A"]==label)|(relaytable_df.loc[:,"Net_A"]==label_c) &(relaytable_df.loc[:,"Net_B"]==snet),"Relay"] = f'K{relay_count}'
                    relay_count +=1
    print("Relay table:")
    print(relaytable_df)



    # find out which relay should be terned on for each test and record in the tabel

    REQ_relay = []

    for r,row in enumerate(Test_plan.values):

        REQ_relay_row = ""        

        for c,model in enumerate(row[1:]):

            if model != "Float":

                a = relaytable_df.loc[:,'Net_A'] == str(head[c])

                b = relaytable_df.loc[:,'Net_B'] == str(model)

                relay = relaytable_df.loc[a & b,"Relay"].values[0]

                REQ_relay_row = REQ_relay_row+","+str(relay)

        REQ_relay_row = REQ_relay_row.lstrip(",")

        REQ_relay.append(REQ_relay_row)

    REQ_relay_df = pd.DataFrame(REQ_relay,columns=["Relay"],index=range(Test_plan.shape[0]))
    Test_plan = pd.concat([Test_plan,REQ_relay_df],axis = 1)#connect two table

    print("Linked relay table:")
    print(Test_plan)    


    #write back to excel

    with pd.ExcelWriter(fileNameStr,engine='openpyxl',mode="a",if_sheet_exists='replace') as writer:
        Test_plan.to_excel(writer,sheet_name = "Sheet3",index=False)

        relaytable_df.to_excel(writer,sheet_name = "Sheet2",index=False)





if __name__ == "__main__":
    main()






import pandas as pd



def main():


    fileNameStr = "RelayTable/RelayTable.xlsx"
    xl = pd.ExcelFile(fileNameStr)
    table = xl.parse('Sheet1')

    relaytable = {}
    head = table.values[0][1:]
    relay_count = 0

    for r,row in enumerate(table.values[1:]):
        for c,model in enumerate(row[1:]):
            line = str(head[c])+"->"+str(model)
            line.lstrip()
            line.rstrip()
            line = line.replace(" ","")
            if not(relaytable.__contains__(line)):
                relaytable[line]=relay_count
                relay_count = relay_count + 1
    print(relaytable)





def hello(name):


    return f"Hello {name}!"




if __name__ == "__main__":
    main()



import xlwings as xw
import numpy as np
import pandas as pd



def main():


    wb = xw.Book.caller()

    Read_in = wb.sheets[0]

    Write = wb.sheets[1]

    table = Read_in.range('A1','H15').value
    relaytable = {}
    head = table[0][1:]
    for r,row in enumerate(table[1:]):
        for c,model in enumerate(row[1:]):
            relaytable[head[c]+"->"+model]=""
    print(relaytable)





@xw.func


def hello(name):


    return f"Hello {name}!"




if __name__ == "__main__":


    xw.Book("RelayTable.xlsm").set_mock_caller()
    main()



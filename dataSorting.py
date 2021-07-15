import pandas as pd


def userInput(self, text):
    while 1:
        try:
            ans = input(text)
            return ans
        except:
            print("Invalid input!")


class dataSorting:
    def __init__(self):
        filepath = userInput("Enter file path: \n")
        xls = pd.ExcelFile(filepath)

    def defaultConfig(self):
        xls = pd.ExcelFile(r"input.xlsx")
        data_column_name = ["Ttb(61-15)",
                            "Tx(61-15)",
                            "Tm(61-11)",
                            "R(61-16)",
                            "Sh(93-07)",
                            "Zn(93-07,12-16)",
                            "U%(93-07)",
                            "Vx(61-2011)",
                            "Umin-(91-015)"]
        self.ttb = xls.parse(data_column_name[0], header=None)
        self.tx = xls.parse(data_column_name[1], header=None)
        self.tm = xls.parse(data_column_name[2], header=None)
        self.r = xls.parse(data_column_name[3], header=None)
        self.sh = xls.parse(data_column_name[4], header=None)
        self.zn = xls.parse(data_column_name[5], header=None)
        self.u = xls.parse(data_column_name[6], header=None)
        self.vx = xls.parse(data_column_name[7], header=None)
        self.umin = xls.parse(data_column_name[8], header=None)
        self.convert_all()

    def convert(self, dataInput, sYear, eYear, yearColumn, rowOffset, columnName):
        output = pd.DataFrame()
        for year in range(sYear, eYear + 1):
            try:
                data = []
                index = dataInput.index[dataInput[yearColumn] == year].tolist()[0]
                dataSet = dataInput.iloc[index + rowOffset:index + 31 + rowOffset, 1:13]
                for month in range(1, 13):
                    data.append(dataSet[month].tolist())
                flat_list = [item for sublist in data for item in sublist]
                newList = [x for x in flat_list if str(x) != 'nan']
                dateIndex = pd.date_range(start='1/1/' + str(year), end='31/12/' + str(year))
                df = pd.DataFrame(dateIndex)
                df[columnName] = newList
                output = output.append(df)
            except Exception as e:
                print(e)
                breakpoint()
        return output

    def convert2(self, dataInput, sYear, eYear, yearColumn, rowOffset, columnName):
        output = pd.DataFrame()
        data = pd.DataFrame()
        for year in range(sYear, eYear + 1):
            dateIndex = pd.DataFrame(pd.date_range(start='1/1/' + str(year), end='31/12/' + str(year)))
            output = output.append(dateIndex)
        output[0] = output[0].dt.date
        for dated in output[0]:
            try:
                index = dataInput.index[dataInput[yearColumn] == dated.year].tolist()[0]
                nrow = index + rowOffset + dated.day - 1
                ncol = dated.month
                dts = pd.DataFrame([str(dataInput.iloc[nrow, ncol])], columns=[columnName])
                data = data.append(dts)
            except Exception as e:
                print(e)
                breakpoint()
        output[columnName] = data[columnName].tolist()
        return output
        dataInput.iloc[1570:1620, 5:8]

        # For each time series find the corresponding value in the sheet

    def convert_all(self):
        output = pd.DataFrame()
        output2 = pd.DataFrame()
        output3 = pd.DataFrame()
        output4 = pd.DataFrame()
        output5 = pd.DataFrame()
        output6 = pd.DataFrame()
        output7 = pd.DataFrame()
        output8 = pd.DataFrame()
        output9 = pd.DataFrame()
        finalOutput = pd.DataFrame()

        output = output.append(self.convert2(self.ttb, 1961, 2006, 0, 2, 'ttb'))
        output = output.append(self.convert2(self.ttb, 2007, 2009, 6, 2, 'ttb'))
        output = output.append(self.convert2(self.ttb, 2010, 2011, 7, 2, 'ttb'))
        output = output.append(self.convert2(self.ttb, 2012, 2014, 0, 1, 'ttb'))
        output = output.append(self.convert2(self.ttb, 2015, 2015, 6, 2, 'ttb'))

        output2 = output2.append(self.convert2(self.tx, 1961, 2004, 0, 2, 'tx'))
        output2 = output2.append(self.convert2(self.tx, 2005, 2006, 0, 1, 'tx'))
        output2 = output2.append(self.convert2(self.tx, 2007, 2008, 6, 2, 'tx'))
        output2 = output2.append(self.convert2(self.tx, 2009, 2009, 7, 2, 'tx'))
        output2 = output2.append(self.convert2(self.tx, 2010, 2010, 6, 2, 'tx'))
        output2 = output2.append(self.convert2(self.tx, 2011, 2011, 0, 1, 'tx'))
        output2 = output2.append(self.convert2(self.tx, 2012, 2015, 6, 2, 'tx'))

        output3 = output3.append(self.convert2(self.tm, 1961, 2005, 0, 2, 'tm'))
        output3 = output3.append(self.convert2(self.tm, 2006, 2006, 0, 1, 'tm'))
        output3 = output3.append(self.convert2(self.tm, 2007, 2008, 6, 2, 'tm'))
        output3 = output3.append(self.convert2(self.tm, 2009, 2009, 7, 2, 'tm'))
        output3 = output3.append(self.convert2(self.tm, 2010, 2010, 6, 2, 'tm'))
        output3 = output3.append(self.convert2(self.tm, 2011, 2011, 0, 1, 'tm'))

        output4 = output4.append(self.convert2(self.r, 1961, 2006, 0, 2, 'r'))
        output4 = output4.append(self.convert2(self.r, 2007, 2016, 6, 2, 'r'))

        output5 = output5.append(self.convert2(self.sh, 1993, 2007, 6, 2, 'sh'))

        output6 = output6.append(self.convert2(self.zn, 1993, 2007, 6, 2, 'zn'))
        output6 = output6.append(self.convert2(self.zn, 2012, 2016, 6, 2, 'zn'))

        output7 = output7.append(self.convert2(self.u, 1993, 2007, 6, 2, 'u%'))

        output8 = output8.append(self.convert2(self.vx, 1961, 2011, 0, 1, 'vx'))

        output9 = output9.append(self.convert2(self.umin, 1991, 2015, 6, 2, 'umin'))

        finalOutput["date"] = output[0]
        finalOutput = finalOutput.set_index("date")
        output = output.set_index(0)
        output2 = output2.set_index(0)
        output3 = output3.set_index(0)
        output4 = output4.set_index(0)
        output5 = output5.set_index(0)
        output6 = output6.set_index(0)
        output7 = output7.set_index(0)
        output8 = output8.set_index(0)
        output9 = output9.set_index(0)

        finalOutput["ttb"] = output["ttb"]
        finalOutput["tx"] = output2["tx"]
        finalOutput["tm"] = output3["tm"]
        finalOutput["r"] = output4["r"]
        finalOutput["sh"] = output5["sh"]
        finalOutput["zn"] = output6["zn"]
        finalOutput["u%"] = output7["u%"]
        finalOutput["vx"] = output8["vx"]
        finalOutput["umin"] = output9["umin"]

        finalOutput.to_csv(r'output.csv')
        print("Done")

    def save(self, data):
        # save the data to file
        pass


dataSorting()

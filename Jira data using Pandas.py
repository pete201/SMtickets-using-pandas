# https://www.linkedin.com/learning/using-python-with-excel/filter-and-sort-with-pandas
## i got to 'filter and sort with pandas' - really good stuff in here!!

import pandas
from openpyxl import workbook
from openpyxl import load_workbook
from openpyxl.utils.cell import get_column_letter
import loadData


inputfile = loadData.readFile()
print("loading file... ",inputfile)
outputfile = "C:/Users/peter.deeming/OneDrive - CMR Surgical Limited/Documents/_4 Output/Monthly Report/2021_FEB Joints awaiting repair pandas01.xlsx"

# create a pandas dataframe from .csv file
df_inputfile = pandas.read_csv(inputfile)

print(df_inputfile.columns,"\n")
print(type(df_inputfile.columns))
print(df_inputfile)
# select list of columns like this:
## double brackets as we present index of df as a list...
print(df_inputfile[["Summary", "Issue key"]])
print()
# select a range of rows like this...
print(df_inputfile[["Summary", "Issue key"]][2:6])
#use ilocation to specify a row,col index...
print(df_inputfile.iloc[2,0])


print()
myColumns = df_inputfile[["Summary", "Issue key", "Issue id", "Custom field (Failed items serial numbers)" ]]
print(myColumns)




# to locate values in data, say find SN = 100...
print(myColumns.loc[myColumns["Custom field (Failed items serial numbers)"] == "40"])

print()
# add new columns...
#GETTING LOTS OF ERRORS IN THIS BLOCK ALTHOUGH IT DOES SORT OF WORK...
myColumns["UID"] = False 
# myColumns["Part Number"] = myColumns["Issue key"] 
# myColumns["Serial Number"] = myColumns["Issue key"] 
# myColumns["Version"] = 0
# myColumns["Notes"] = 0

print("now the column headings are...")
print(myColumns.columns)

# output to an Excel file
#df_inputfile.to_excel(outputfile)
myColumns.to_excel(outputfile)
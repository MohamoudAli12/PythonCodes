import openpyxl
def createFile():
    global fileName, newFile
    fileName=input('Enter file name:')
    newFile=open(fileName,'w+b')
    newFile.close()

def writeFile():
    global fileName, newFile, userInput
    fileName=input('Enter file name you want to wrtie to:')
    newFile=open(fileName,'w+b')
    newFile.write(userInput)
    newFile.close()

createFile()

workbook= openpyxl.load_workbook('malik.xlsx')
sheet =workbook.get_sheet_by_name('Sheet2')
cell =sheet['C2']
userInput=bytes(cell.value,'utf-8')

writeFile()

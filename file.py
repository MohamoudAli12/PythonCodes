def createFile():
    global fileName, newFile
    fileName=input('Enter file name:')
    newFile=open(fileName,'w+b')

def writeFile():
    global fileName, newFile
    fileName=input('Enter file name you want to wrtie to:')
    newFile=open(fileName,'w')
    userInput=input('Enter text you want to save:')
    newFile.write(userInput)

def readFile():
    global fileName, newFile
    fileName=input('Enter file name you want to read:')
    newFile=open(fileName,'r')
    print('you chose to read file:',fileName)
    content=newFile.read()
    print('*************************************************')
    print(content)
    print('*************************************************')

def closeFile():
    newFile.close()

cond='yes'
cond1='yes'

print('''
*****************************************
*****************************************
Welcome to file creator and editor:
1. Create file
2. Write to file
3. Read file
*****************************************
*****************************************
''')
while cond=='yes':
    userChoice=input('Choose 1,2 or 3: ')
    if int(userChoice)==1:
        print("you chose to create a file:")
        createFile()
        print("Thank you! the file:",fileName,"is created")
        closeFile()
    elif int(userChoice)==2:
        print('you chose to write to a file:')
        writeFile()
        closeFile()
    elif int(userChoice)==3:
        readFile()
        closeFile()
    while cond1=='yes':
        cond1=input('Do you want to continue(yes or no):')
        if cond1=='yes':
            cond='yes'
            break
        elif cond1== 'no':
            cond='no'
            cond1='no'
        else:
            print('Invalid Input')
            cond1='yes'
print ('Thank You!!!!!')

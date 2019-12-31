import csv # Comma(delimiters) separated variables

makeExCsv = open('csvExampleFile.csv', 'w')

makeExCsv.write('col1, col2, col3\ndata1, data2, data3\ndata4, data5, data6\ndata7, data8, data9')

makeExCsv.close()

col1 = []
col2 = []
col3 = []

with open('csvExampleFile.csv') as varToRecallOpen: # varToRecallOpen stores file name with open command. With open is like a function.

    varToStoreReferenceOfDataOfCsv = csv.reader(varToRecallOpen, delimiter = ',')

    for i in varToStoreReferenceOfDataOfCsv:
        print(i)
        print(i[0])
        print(i[0], i[1])
        col1Data = i[0]
        col2Data = i[1]
        col3Data = i[2]
        #print('This 1:', col2Data)
        #print('This 2:', col2Data)
        #print('This 3:', col3Data)

        col1.append(col1Data)
        col2.append(col2Data)
        col3.append(col3Data)

    """ # This is not working
    for j in varToStoreReferenceOfDataOfCsv:
        col1Data = j[1]
        col2Data = j[2]
        print('This 1:',col2Data)
        print('This 2:',col2Data)

        col1.append(col1Data)
        col2.append(col2Data)
    """
    print(col1)
    print(col2)
    print(col3)

    varInput = input('Type the column you want data of: ')

    if varInput == 'col1' :
        print(col1)
    if varInput == 'col2':
        print(col2)
    if varInput == 'col3':
        print(col3)

makeExCsv.close()
# import csv
##reading from csv file
# with open('C:\Users\Vadim\Projects\Python\Test_CSV2.csv') as csvfile:
#     readCSV = csv.reader(csvfile, delimiter=',')
#     for row in readCSV:
#         print(row[0], row[3])
#=====================================================================================
import csv

with open('C:\Users\Vadim\Projects\Python\Test_CSV2.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
#create separate list of extracted values from csv file
    dates = []
    colors = []

    for row in readCSV:
        color = row[3]
        colors.append(color)
        date = row[0]
        dates.append(date)
    print(dates)
    print(colors)

    try:          #try this code, if there is a problem, go to except part
        whatColor = input('What color do you wish to know the date of?')
        if whatColor in colors:
            coldex = colors.index(whatColor.lower())    #lower() just to make the responce lower case as all colors in lower case
            theDate = dates[coldex]
            print('The date of ' + whatColor + ' is: ' + theDate)
        else:
            print('Color is not found')
    except Exception as e:   #Exception could be NameError or ValueError
        print(e)

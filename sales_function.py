#delcare imports
import  os
import csv

#Path to collect the data from
salesCSV = os.path.join("..", "S-P-500-Financial-Stats", "Sales-Data-2016.csv")

#Define the function and have it accept 'salesData' as its sole parameter
def getFinancials(salesData):
    #Netincome can be found by Revenue - Expenses
    netIncome = int(salesData[1]) - int(salesData[2])

    #Profit margin equals Revenue/  NetIncome(Revenue-Expenses)
    profitMargin = int(salesData[1])/netIncome

    #Net Assets equals Assets - Liabilities
    netAsset = int(salesData[3]) - int(salesData[4])

    #Asset to Liability ratio equals assets/ net assets
    assetRatio = int(salesData[3])/ netAsset

    #Shareholders equality equals Net Assest
    shareholdersEquality = int(salesData[3]) - int(salesData[4])

    #If NetIncome is greater than 0, Co is NetIncome Positive, if equal 0, Broke even, else negative

    if (netIncome == 0):
        typeOfIncome = "Net Income even"

    elif (netIncome > 0):
        typeOfIncome = "Net Income Positive"

    else:
        typeOfIncome= "Net Income Negative"

    #If Net Assets greater than 0, Net asset positive, equal 0, else negative

    if (netAsset == 0):
        typofAsset = "Net Asset even"
    elif (netAsset > 0):
        typofAsset = "Net Asset positive"
    else:
        typofAsset = "Net Asset negative"

    #Print out the Company's name and their financial stats
    print(f"Financial Stats for {salesData[0]}")
    print(f"NET INCOME: ${str(netIncome)}")
    print(f"PROFIT MARGIN: {str(profitMargin)}%")
    print(f"NET ASSET: ${str(netAsset)}")
    print(f"ASSET TO LIABILITY RATIO: {str(assetRatio)}%")
    print(f"Shareholders Equity: ${str(shareholdersEquality)}")
    print(f"{salesData[0]} is {typeOfIncome} and {typofAsset}")
print ("-----------------------------------------------------------------------------------------------------")

#Set variable to check if company found
found = False
#Read in CSV File

with open(salesCSV, 'r') as csvfile:

    #Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvfile)

    #Prompt the user for the S&P 500 company they would like to search
    companyToCheck = input("What S&P 500 Company do you want to look for? ")

    #Loop through the data

    for row in csvreader:
        #If the company's name in a row is equal to that which is input...
        if (row[0] == companyToCheck):
            getFinancials(row)
            found = True

        #If we company never found, alert user
    if found == False:
        print("Sorry. We do not have that company on file.")



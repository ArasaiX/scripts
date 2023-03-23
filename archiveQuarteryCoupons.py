import csv
import requests
import json

#First message, global variables (input), and open the file to write the results

print("\nThis script helps you by archiving the quarterly VTEX coupons entered in a csv file.\nRemember to locate the csv file in the same directory where you run the script.\n")
vtexAPIKey = input("Enter the vtexAPIKey: ")
vtexAPIToken = input("\nEnter the vtexAPIToken: ")
csvFile = input("\nEnter the name of csv to read(with the extension): ")
outputFile= open("output.txt", "w")

# Fill out this two variables before run the script
accountName = ''
environment = ''

headers= {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-VTEX-API-AppKey": vtexAPIKey,
    "X-VTEX-API-AppToken": vtexAPIToken
}

#Main function

def main():

    print("\n>>>>>> Executing script\n")
    with open(csvFile, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            couponCode = row[2] #this is 2, change if the column of code in csv is another
            outputFile.write(f"\n>Coupon {couponCode}: ")
            CheckIfCouponExistInVTEX(couponCode)
        print("Done! You can read a report with the results in the output.txt file")

            
#Check if coupon exist calling API from VTEX. If exists go to check if coupon is archived

def CheckIfCouponExistInVTEX(couponCode):
    
    url = f'https://{accountName}.{environment}.com.br/api/rnb/pvt/coupon/{couponCode}'
    response = requests.get(url, headers=headers)
    if (response.status_code == 200):
        data = response.text
        json_data = json.loads(data)
        CheckIfCouponWasArchivedInVTEXBefore(json_data, couponCode)

    elif (response.status_code == 401):
        outputFile.write(f"Unauthorized. Status code: {response.status_code} \n")
        
    elif (response.status_code == 404):
        outputFile.write(f"Coupon not found. Status code: {response.status_code} \n")
        
    else:
        outputFile.write(f"Error {response.status_code} \n")
        

#Function that reads the data and decide if the coupon must be archived

def CheckIfCouponWasArchivedInVTEXBefore(json_data, couponCode):

    url = f'https://{accountName}.{environment}.com.br/api/rnb/pvt/archive/coupon/{couponCode}'
    response = requests.get(url, headers=headers)
    if (response.status_code == 200):
        data = response.text
        json_data = json.loads(data)
        
        if ((json_data['isArchived']) == True):
            outputFile.write(f"This coupon is already archived! (Campaign: {json_data['utmCampaign']}) \n")
            
        else:
            outputFile.write(f"Let's archive it! (Campaign: {json_data['utmCampaign']}) \n")
            archiveCouponInVtex(couponCode)

    else:
        outputFile.write(f"Error {response.status_code} \n")
    

#Archive coupon

def archiveCouponInVtex(couponCode):

    url = f'https://{accountName}.{environment}.com.br/api/rnb/pvt/archive/coupon/{couponCode}'
    response = requests.post(url, data=couponCode, headers=headers)

    if response.status_code == 200:
        outputFile.write("Successfully archived \n")
    else:
        outputFile.write(f"Post failed. Status code: {response.status_code} \n")


main()
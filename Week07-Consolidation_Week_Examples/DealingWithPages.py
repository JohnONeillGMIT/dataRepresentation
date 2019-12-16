import requests
import json
from xlwt import *

#url= "https://reports.sem-o.com/api/v1/documents/static-reports"
url= "https://reports.sem-o.com/api/v1/documents/static-reports?ReportName=Balancing%20&Date=>2019-12-12"
response=requests.get(url)
data=response.json()
totalPages=data["pagination"]["totalPages"]
print(totalPages)
listOfReports=[]

#getting all the page Numbers to print
pageNumber=1
while pageNumber <= totalPages:
    pageUrl =url + "&page="+str(pageNumber)
    #print(pageUrl)
    data=requests.get(pageUrl).json()
    for item in data["items"]:
        #print(item["ResourceName"])
        listOfReports.append(item["ResourceName"])
    pageNumber +=1

#output to console
#print (data)
for reportName in listOfReports:
    print(reportName)


filename="allReports.json"
f=open(filename,'w')
json.dump(data,f,indent=4)


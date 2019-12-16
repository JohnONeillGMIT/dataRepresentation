import requests
import json

#url= "https://reports.sem-o.com/api/v1/documents/static-reports"
url= "https://reports.sem-o.com/api/v1/documents/static-reports?ReportName=Balancing%20&Date=>2019-12-12"
response=requests.get(url)
data=response.json()

#output to console
print (data)

#other code
#save this to a file
filename='allreports.json'
#Writing JSON data
f=open(filename,'w')
json.dump(data,f,indent=4)

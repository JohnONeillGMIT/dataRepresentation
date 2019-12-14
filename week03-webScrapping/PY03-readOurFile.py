from bs4 import BeautifulSoup

with open("C:/Users/john_j_o'neill/DataRepresentation/week03-webScrapping/carviewer02.html") as fp:
    soup = BeautifulSoup(fp,'html.parser')


#print (soup.tr)
#print all the rows under each tr
rows= soup.findAll('tr')
for row in rows:
#    print(row)
    dataList =[]
    cols =row.findAll("td")
    for col in cols:
        dataList.append(col.text)
    print(dataList)

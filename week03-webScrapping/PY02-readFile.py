from bs4 import BeautifulSoup

with open("C:/Users/john_j_o'neill/DataRepresentation/week03-webScrapping/carviewer02.html") as fp:
    soup = BeautifulSoup(fp,'html.parser')

#soup1 = BeautifulSoup(page.content.'html.parser')

#print("----------------")
#print(page.content)
#soup1 = BeautifulSoup(page.content,'html.parser')
print (soup.prettify())
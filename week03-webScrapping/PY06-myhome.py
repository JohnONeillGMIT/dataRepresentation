import requests 

from bs4 import BeautifulSoup
page = requests.get("https://www.myhome.ie/residential/clare-1/property-for-sale") 
 
soup = BeautifulSoup(page.content, 'html.parser') 
#print (soup.prettify())

#listings = soup.find("div", class_="PropertyListingCard" ) 
#print (listings) 

#price = listings.find(class_="PropertyListingCard__Price").text 
 
#print (price) 

listings = soup.findAll("div", class_="PropertyListingCard" ) 
 
for listing in listings:  
    entry = []    
    price = listing.find(class_="PropertyListingCard__Price").text   
    entry.append(price)
    address = listing.find(class_="PropertyListingCard__Address").text   
    entry.append(address) 
print(entry) 
 
 

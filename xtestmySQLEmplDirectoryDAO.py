from mySQLEmplDirectoryDAO import emplDirectoryDAO

#create
latestid = emplDirectoryDAO.create(('Adam','Clayton',2008))

#find by id
result = emplDirectoryDAO.findByID(latestid); 
print (result)

#update
emplDirectoryDAO.update(('Larry','Mullen',3458,latestid))
result = emplDirectoryDAO.findByID(latestid);
print (result)

#getall
allEmployees = emplDirectoryDAO.getAll()
for employee in allEmployees:
    print(employee)

#delete
emplDirectoryDAO.delete(latestid)

#  IT WORKS!! I HATE CASE SENSITIVE!!!
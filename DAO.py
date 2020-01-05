#IT WORKS!!!!!!!!!!! 04/01/2020
import mysql.connector
import dbconfig as cfg
# creating a Class
class EmplDirDAO:
    db=""
    def __init__(self):
        self.db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database =   'datarepresentation2',
        auth_plugin="mysql_native_password"
        )
    def create(self,values):
        cursor = self.db.cursor()
        sql = "insert into empldirectory (first_name,surname,Ext) values (%s,%s,%s)"
        cursor.execute(sql,values)

        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql ="select * from empldirectory"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            returnArray.append(self.convertToDictionary(result))

        return returnArray

    def findByID(self,id):
        cursor = self.db.cursor()
        sql = "select * from empldirectory where id = %s"
        values = (id,)

        cursor.execute(sql,values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)

    def update(self,values):
        cursor = self.db.cursor()
        sql ="update empldirectory set first_name= %s,surname= %s, Ext= %s where id= %s"
        cursor.execute(sql,values)
        self.db.commit()
        print("update done")

    def delete(self,id):
        cursor = self.db.cursor()
        sql = "delete from empldirectory where id = %s"
        values = (id,)

        cursor.execute(sql,values)
        self.db.commit()
        print("delete done")

    def convertToDictionary(self,result):
        colNames=['id','first_name','surname','Ext']
        item = {}

        if result:
            for i, colName in enumerate(colNames):
                value = result[i]
                item[colName] =value
        
        return item

emplDirectoryDAO = EmplDirDAO()
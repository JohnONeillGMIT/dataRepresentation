import mysql.connector
# creating a Class
class EmplDirectoryDAO:
    db=""
    def __init__(self):
        self.db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database ="datarepresentation",
        auth_plugin="mysql_native_password"
        )
    def create(self,values):
        cursor = self.db.cursor()
        sql = "insert into Empldirectory (first_name,surname,Ext) values (%s,%s,%s)"
        cursor.execute(sql,values)

        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql ="select * from EmplDirectory"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def findByID(self,id):
        cursor = self.db.cursor()
        sql = "select * from EmplDirectory where id = %s"
        values = (id,)

        cursor.execute(sql,values)
        result = cursor.fetchone()
        return result

    def update(self,values):
        cursor = self.db.cursor()
        sql ="update EmplDirectory set first_name= %s,surname=%s,Ext=%s where id= %s"
        cursor.execute(sql, values)
        self.db.commit()

    def delete(self,id):
        cursor = self.db.cursor()
        sql = "delete from EmplDirectory where id = %s"
        values = (id,)

        cursor.execute(sql,values)
        self.db.commit()
        print("delete done")

emplDirectoryDAO = EmplDirectoryDAO()
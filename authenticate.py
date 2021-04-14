import mysql.connector as sqltor

class Authenticate:
    def __init__(self,username,passwd):
        self.username = username
        self.passwd = passwd
        
        
    def auth(self):
        mycon = sqltor.connect(host = "localhost",user = "root",passwd = "qwerty",database = "authenticate")
        cursor = mycon.cursor()
        cursor.execute("select passwd from users where username = \"{}\";".format(self.username))
        data = cursor.fetchone()
        if (self.passwd == data[0]):
            print("Validated")
            mycon.commit()
            mycon.close()
            return True
        else:
            print("Invalid password")
            mycon.commit()
            mycon.close()
            return False
    
    def createUser(self):
        mycon = sqltor.connect(host = "localhost",user = "root",passwd = "qwerty",database = "authenticate")
        cursor = mycon.cursor()
        cursor.execute("insert into users values (\"{}\",\"{}\");".format(self.username,self.passwd))
        mycon.commit()
        mycon.close()
    
    def deleteUser(self):
        mycon = sqltor.connect(host = "localhost",user = "root",passwd = "qwerty",database = "authenticate")
        cursor = mycon.cursor()
        cursor.execute("delete from users where username = \"{}\"".format(self.username))
        mycon.commit()
        mycon.close()
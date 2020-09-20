from flask_mysqldb import MySQL
import MySQLdb


def read(mysql,Email,Password):
    cur = mysql.connection.cursor()
    try:
        cur.execute(f"Select username From accounts Where mail = '{Email}' And password = '{Password}'")
        mysql.connection.commit()
        result = cur.fetchone()
        return result  

    finally:
        cur.close()


def insert(mysql,UserName,Email,Password,Password2):
    if Password == Password2:
        cur = mysql.connection.cursor()
        try:
            cur.execute("INSERT INTO accounts(username,password,mail) VALUES (%s, %s, %s)", (UserName, Password, Email))
            mysql.connection.commit()
            return "Success"

        except TypeError:
            return "AlreadyExists"

        except:
            return None 

        finally:
            cur.close()   

        return "Password Match"
    
    else:
        return "PasswordError"



def delete(mysql,Email):
        cur = mysql.connection.cursor()
        try:
            cur.execute(f"Delete From accounts Where mail = '{Email}'")
            mysql.connection.commit()

        except TypeError:
            return "AlreadyExists"    
            
        except:
            return None 

        finally:
            cur.close()


def update(mysql,UserName,Email,Password):
        cur = mysql.connection.cursor()
        try:
            query = f""" UPDATE accounts
                    SET username = '{UserName}', password = '{Password}'
                    WHERE mail = '{Email}' """

            cur.execute(query)
            mysql.connection.commit()
        
        except TypeError:
            return "AlreadyExists"    
                
        except:
            return None 

        finally:
            cur.close()

def readFID(mysql,PicName):
    cur = mysql.connection.cursor()
    try:
        cur.execute(f"Select username,email From faceid Where picname = '{PicName}'")
        mysql.connection.commit()
        result = cur.fetchone()
        return result  

    finally: 
        cur.close()


def insertFID(mysql,UserName,PicName,Email):
    cur = mysql.connection.cursor()
    try:
        cur.execute("INSERT INTO faceid(username,picname,email) VALUES (%s, %s,%s)", (UserName, PicName,Email))
        mysql.connection.commit()
        return "Success"

    except TypeError:
        return "AlreadyExists"

    except:
        return None 

    finally:
        cur.close()   

   
    
   



def deleteFID(mysql,PicName):
        cur = mysql.connection.cursor()
        try:
            cur.execute(f"Delete From faceid Where picname = '{PicName}'")
            mysql.connection.commit()

        except TypeError:
            return "AlreadyExists" 

        except:
            return None 

        finally:
            cur.close()


def updateFID(mysql,UserName,PicName):
        cur = mysql.connection.cursor()
        try:
            query = f""" UPDATE faceid
                    SET username = '{UserName}'
                    WHERE picname = '{PicName}' """

            cur.execute(query)
            mysql.connection.commit()

        except TypeError:
            return "AlreadyExists"

        except:
            return None 

        finally:
            cur.close()


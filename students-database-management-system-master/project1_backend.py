import mysql.connector
#import project1_frontend

def studentData():
        con = mysql.connector.connect(host="localhost",user="root",password="root",database="project")
        cur=con.cursor()
       
        cur.execute("CREATE TABLE IF NOT EXISTS priyag(StdID text,Firstname text,Surname text,DoB text,Age text,Gender text,Address text,Mobile text)")
        con.commit()
        con.close()              
def addStdRec(StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile):
        con=con = mysql.connector.connect(host="localhost",user="root",passwd="root")
        cur=con.cursor()
        cur.execute("use project")
        cur.execute("INSERT INTO priyag VALUES(null,%s,%s,%s,%s,%s,%s,%s,%s)",(StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile))
        con.commit()
        con.close() 
def viewData():
        con=con = mysql.connector.connect(host="localhost",user="root",passwd="root")
        cur=con.cursor()
        cur.execute("use project")
        cur.execute("select * from priyag")
        row=cur.fetchall()
        con.close()       
        return row
def deleteRec(id):
        con=con = mysql.connector.connect(host="localhost",user="root",passwd="root")
        cur=con.cursor()
        cur.execute("use project")
        cur.execute("DELETE  FROM priyag WHERE id=%s",(id,))
        con.commit()
        con.close()         
def searchData(StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile):
        con=con = mysql.connector.connect(host="localhost",user="root",passwd="root")
        cur=con.cursor()
        cur.execute("use project")
        cur.execute("SELECT * FROM priyag WHERE StdID=%s or Firstname=%s or Surname=%s or DoB=%s or Age=%s or Gender=%s or Address=%s or Mobile=%s",(StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile))
        rows=cur.fetchall()
        con.close()        
        return rows
def dataUpdate(id,StdID="",Firstname="",Surname="",DoB="",Age="",Gender="",Address="",Mobile=""):
        con = mysql.connector.connect(host="localhost",user="root",passwd="#root")
        cur=con.cursor()
        cur.execute("use project")
        cur.execute("UPDATE priyag SET StdID=%s,Firstname=%s,Surname=%s,DoB=%s,Age=%s,Gender=%s,Address=%s,Mobile=%s WHERE id=%s",(StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile))
        con.commit()
        con.close()    

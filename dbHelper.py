
import pyodbc
from Amazon2 import dbModels
from .dbModels import postModel, userModel
class dbHelper:
    #Class used to read and write to sql server database.
    
    #Adds new user with supplied properties

    def addNewUser(email,username,password):

        conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                              'Server=(localdb)\MSSQLLocalDB;'
                              'Database=Backroom;'
                              'Trusted_Connection=yes;')
        cursor = conn.cursor()
        count = cursor.execute('''Select Count(EmailID) FROM Backroom.dbo.Users WHERE EmailID = ?''', email)
        if count.arraysize > 0:
            return 1
        cursor.execute('''INSERT into Backroom.dbo.Users VALUES(?,?,?)''',email,username,password)
        conn.commit()
        return 0

    #Returns true or false based on if supplied args match db properties
    def login(name,pword):
        logged_in = False
        conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                              'Server=(localdb)\MSSQLLocalDB;'
                              'Database=Backroom;'
                              'Trusted_Connection=yes;')
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM Backroom.dbo.Users WHERE UserName =? AND Password =?''',name,pword)

        for row in cursor:
            logged_in = True
        return logged_in
    
    #Adds new item with supplied arguments
    def addItem(auth,title,desc,loc,price):
        conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                              'Server=(localdb)\MSSQLLocalDB;'
                              'Database=Backroom;'
                              'Trusted_Connection=yes;')
        cursor = conn.cursor()
        cursor.execute('''INSERT into Backroom.dbo.Post(Author,Title,"Desc","Location",Price) VALUES(?,?,?,?,?)''',auth,title,desc,loc,price)
        conn.commit()
        
    #Returns single post item based on id
    def getItemById(ID):
        conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                              'Server=(localdb)\MSSQLLocalDB;'
                              'Database=Backroom;'
                              'Trusted_Connection=yes;')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Backroom.dbo.Post WHERE PostID =?',ID)

        for row in cursor:
            post = postModel(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
            return post

    #Deletes item by id
    def deleteItemById(ID):
        conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                              'Server=(localdb)\MSSQLLocalDB;'
                              'Database=Backroom;'
                              'Trusted_Connection=yes;')
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM Backroom.dbo.Post WHERE PostID=?''',ID)
        conn.commit()
    
    #Returns list of all posts
    def getAllItems():
        conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                              'Server=(localdb)\MSSQLLocalDB;'
                              'Database=Backroom;'
                              'Trusted_Connection=yes;')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Backroom.dbo.Post')
        posts = []
        for row in cursor:
            post = postModel(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
            posts.append(post)
        return posts

    def searchByTitle(value):
        conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                              'Server=(localdb)\MSSQLLocalDB;'
                              'Database=Backroom;'
                              'Trusted_Connection=yes;')
        cursor = conn.cursor()
        sql = 'SELECT * FROM Backroom.dbo.Post WHERE Title LIKE %sand%'
        args = [value]
        cursor.execute(sql)
        posts = []
        for row in cursor:
            post = postModel(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
            posts.append(post)
        return posts
    
    #method to get all current categories

    #method to join post with new catagories table





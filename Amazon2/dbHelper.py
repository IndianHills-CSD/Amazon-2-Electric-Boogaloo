import pyodbc 
class dbHelper:
    """Class used to read and write to sql server database."""

    def addNewUser():
        conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                              'Server=(localdb)\MSSQLLocalDB;'
                              'Database=Backroom;'
                              'Trusted_Connection=yes;')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM TAL_Test.dbo.Post')

        for row in cursor:
            print(row)


    def login():
        conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                              'Server=(localdb)\MSSQLLocalDB;'
                              'Database=Backroom;'
                              'Trusted_Connection=yes;')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Backroom.dbo.Post')

        for row in cursor:
            print(row)

    def addItem():
        conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                              'Server=(localdb)\MSSQLLocalDB;'
                              'Database=Backroom;'
                              'Trusted_Connection=yes;')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Backroom.dbo.Post')

        for row in cursor:
            print(row)

    def getAllItems():
        conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                              'Server=(localdb)\MSSQLLocalDB;'
                              'Database=Backroom;'
                              'Trusted_Connection=yes;')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Backroom.dbo.Post')

        for row in cursor:
            print(row)

    def getItemById(ID):
        conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                              'Server=(localdb)\MSSQLLocalDB;'
                              'Database=Backroom;'
                              'Trusted_Connection=yes;')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Backroom.dbo.Post WHERE PostID =?',ID)

        for row in cursor:
            print(row)
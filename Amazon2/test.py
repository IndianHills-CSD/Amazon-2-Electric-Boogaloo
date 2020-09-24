import pyodbc

conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                      'Server=(localdb)\MSSQLLocalDB;'
                      'Database=TAL_Test;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('''INSERT INTO TAL_Test.dbo.ITEM (ITEM_NUM, DESCRIPTION, ON_HAND, CATEGORY, STOREHOUSE, PRICE) VALUES ('BB42', 'Toy Gun', 10, 'TOY', 1, 19.99)''')


conn.commit()

cursor.execute('SELECT * FROM TAL_Test.dbo.ITEM')

for row in cursor:
    print(row)



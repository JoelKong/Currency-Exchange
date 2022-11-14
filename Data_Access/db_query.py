import pyodbc

#Make connection to sql
def create_connection():
    conn = None
    try:
        conn = pyodbc.connect("driver={SQL Server};"
                        "server=LAPTOP-6I8KKLOH;"
                        "database=Definite;"
                        "trusted_connection=yes;")
        print ("Connection to SQL Server successful")
    except pyodbc.Error as e:
        print(f"The error '{e}' occurred")
    return conn

#Execute query
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except pyodbc.Error as e:
        print(f"The error '{e}' occurred")

#Commit the transaction info/receipt
def execute_query_commit(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed and committed. You can view the transaction details in the database.")
    except pyodbc.Error as e:
        print(f"The error '{e}' occurred")

#Commit the update information of sender
def execute_update_query_commit(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except pyodbc.Error as e:
        print(f"The error '{e}' occurred")
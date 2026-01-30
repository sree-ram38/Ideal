import mysql.connector

try:
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user = "root",
        password = "S@123",
        database = "school"
    )
    if conn.is_connected():
        print("Connected to the database")
    else:
        print("Failed to connect to the database")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if conn.is_connected():
        conn.close()
    print("Connection closed")
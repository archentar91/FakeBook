# Install Mysql on your system

import mysql.connector
from mysql.connector import Error

def connect_to_database():
    try:
        # MySQL credentials
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="113265",
            database="mydatabase"
        )
        return connection
    except Error as error:
        print("Error while connecting to MySQL:", error)
        return None

def close_connection(connection):
    if connection:
        connection.close()

def main():
    # Connecting to the MySQL database
    connection = connect_to_database()

    if connection:
        try:
            # Create a cursor object to interact with the database
            cursor = connection.cursor()

            # Execute a sample query
            cursor.execute("SELECT version();")

            # Fetch the query result
            result = cursor.fetchone()

            print("MySQL database version:")
            print(result)

        except Error as error:
            print("Error while executing query:", error)

        finally:
            # Close the cursor and connection
            cursor.close()
            close_connection(connection)

if __name__ == "__main__":
    main()

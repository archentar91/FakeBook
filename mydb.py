# Install Mysql on your system
#pip install psycopg2


import psycopg2
from psycopg2 import Error

def connect_to_database():
    try:
        # PostgreSQL credentials
        connection = psycopg2.connect(
            user = "postgres",
            password = "113265",
            host = "localhost",
            database = "db2",
            port = "5432"
        )
        return connection
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL:", error)
        return None

def close_connection(connection):
    if connection:
        connection.close()

def main():
    # Connecting to the PostgreSQL database
    connection = connect_to_database()

    if connection:
        try:
            # Create a cursor object to interact with the database
            cursor = connection.cursor()

            # Execute a sample query
            cursor.execute("SELECT version();")

            # Fetch the query result
            result = cursor.fetchone()

            print("PostgreSQL database version:")
            print(result)

        except (Exception, Error) as error:
            print("Error while executing query:", error)

        finally:
            # Close the cursor and connection
            cursor.close()
            close_connection(connection)

if __name__ == "__main__":
    main()
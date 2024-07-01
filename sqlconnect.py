import psycopg2
from psycopg2 import sql

# Database connection parameters
db_config = {
    'dbname': 'your_database_name',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'your_host',
    'port': 'your_port'  # Default PostgreSQL port is 5432
}

try:
    # Establishing the connection
    conn = psycopg2.connect(**db_config)
    print("Connection established successfully.")

    # Creating a cursor object to interact with the database
    cursor = conn.cursor()

    # Example query to fetch data
    cursor.execute(sql.SQL("SELECT * FROM your_table_name"))
    records = cursor.fetchall()

    for row in records:
        print(row)

    # Closing the cursor and connection
    cursor.close()
    conn.close()
    print("Connection closed.")

except Exception as error:
    print(f"Error connecting to the database: {error}")
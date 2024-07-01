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

def insert_row(table_name, column_values):
    """
    Inserts a new row into the specified table.

    :param table_name: Name of the table where the row will be inserted.
    :param column_values: A dictionary containing column-value pairs to be inserted.
    """
    try:
        # Establishing the connection
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()
        
        # Generating the SQL query
        columns = column_values.keys()
        values = [column_values[col] for col in columns]
        insert_query = sql.SQL("INSERT INTO {table} ({fields}) VALUES ({values})").format(
            table=sql.Identifier(table_name),
            fields=sql.SQL(', ').join(map(sql.Identifier, columns)),
            values=sql.SQL(', ').join(sql.Placeholder() * len(values))
        )
        
        # Executing the query
        cursor.execute(insert_query, values)
        conn.commit()
        
        print("Row inserted successfully.")
        
        # Closing the cursor and connection
        cursor.close()
        conn.close()
        
    except Exception as error:
        print(f"Error inserting row into the database: {error}")

# Example usage
table_name = 'your_table_name'
column_values = {
    'column1': 'value1',
    'column2': 'value2',
    # Add more column-value pairs as needed
}

insert_row(table_name, column_values)
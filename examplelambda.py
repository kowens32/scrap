import os
import json
import psycopg2
from psycopg2.extras import RealDictCursor

def lambda_handler(event, context):
    # Database connection parameters from environment variables
    db_host = os.getenv('DB_HOST')
    db_name = os.getenv('DB_NAME')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_port = os.getenv('DB_PORT', 5432)

    # Establish a connection to the database
    try:
        conn = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_password,
            port=db_port
        )
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Database connection failed: {str(e)}")
        }

    # Create a cursor object using RealDictCursor to get dictionary output
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    # Sample query to read data from the database
    query = "SELECT * FROM your_table_name LIMIT 10;"

    try:
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return {
            'statusCode': 200,
            'body': json.dumps(result, default=str)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Query execution failed: {str(e)}")
        }

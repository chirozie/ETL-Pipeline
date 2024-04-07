import clickhouse_connect
import psycopg2
from dotenv import dotenv_values


# config = dict(dotenv_values())

def get_client():
    '''
    
    '''
    config = dict(dotenv_values())

  #setting DB connection parameters - Clickhouse
    host =  config.get('host')
    port = config.get('port')
    user = config.get('user')
    password = config.get('password')

    # Connect to ClickHouse database
    client = clickhouse_connect.get_client(host=host, port=port, user=user, password=password)

    return client
    





def get_postgres_connection():
    config = dict(dotenv_values())
    """
    Get connection and cursor to the PostgreSQL database using parameters from .env file.

    Returns:
        tuple: Connection and cursor objects.
    """
     
    # connection parameters 
    connection_params = {
        'host': config.get('pg_host'),
        'port': config.get('pg_port'),
        'database': config.get('pg_database'),
        'user': config.get('pg_user'),
        'password': config.get('pg_password')
    }

    # Connect to the PostgreSQL database
    conn = psycopg2.connect(**connection_params)
    cursor = conn.cursor()
    
    return conn, cursor
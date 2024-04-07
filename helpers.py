import clickhouse_connect
import psycopg2

def get_client():
    '''
    
    '''
  #setting DB connection parameters - Clickhouse
    host =  'github.demo.trial.altinity.cloud'
    port = 8443
    user = 'demo'
    password = 'demo'

    # Connect to ClickHouse database
    client = clickhouse_connect.get_client(host=host, port=port, user=user, password=password)

    return client
    





def get_postgres_connection():
    """
    Get connection and cursor to the PostgreSQL database using parameters from .env file.

    Returns:
        tuple: Connection and cursor objects.
    """

    # connection parameters 
    connection_params = {
        'host': 'localhost',
        'port': '5432',
        'database': 'DivyTrips',
        'user': 'postgres',
        'password': '55668833rozy'
    }

    # Connect to the PostgreSQL database
    conn = psycopg2.connect(**connection_params)
    cursor = conn.cursor()
    
    return conn, cursor
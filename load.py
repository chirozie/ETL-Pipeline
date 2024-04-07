from helpers import get_postgres_connection

def load_csv_to_postgres(csv_file_path, table_name):
    """
    Load data from a CSV file into a PostgreSQL table using the COPY command.

    Parameters:
        csv_file_path (str): Path to the CSV file.
        table_name (str): Name of the PostgreSQL table to load the data into.

    Returns:
        bool: True if the data was successfully loaded, False otherwise.
    """
    # Get connection and cursor
    conn, cursor = get_postgres_connection()

    # Create COPY command to load data from CSV file
    copy_sql = f"""
                COPY {table_name} FROM stdin WITH CSV HEADER
                DELIMITER ','
                """

    # Open the CSV file and execute the COPY command
    with open(csv_file_path, 'r') as f:
        cursor.copy_expert(sql=copy_sql, file=f)
        conn.commit()
    
    # Close cursor and connection
    cursor.close()
    conn.close()
    
    print("Data loaded successfully.")
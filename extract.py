# importing libraries
import pandas as pd


# Function 1 - fetch metrics and insert into SQLite DB
def fetch_data(client):
    '''
    
    '''
    
    
    # Query for metrics data 
    clickhouse_query = """
    SELECT pickup_datetime, dropoff_datetime, passenger_count, trip_distance, payment_type, fare_amount, tip_amount
    FROM tripdata
    WHERE year(pickup_date) = 2015
            """

    # Fetch metrics data
    clickhouse_result = client.query(clickhouse_query)
    rows = clickhouse_result.result_rows

    
    # Close the connection
    client.close()

    #write data to csv
    df = pd.DataFrame(rows, columns=['pickup_datetime', 'dropoff_datetime', 'passenger_count', 
                                        'trip_distance', 'payment_type', 'fare_amount', 'tip_amount'])


    print(len(df))


    df.to_csv('tripdata.csv', index=False)
    
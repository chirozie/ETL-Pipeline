from dotenv import load_dotenv
import os

#Importing custom fuctions - metric query function and truncate SQLite DB function
from extract import fetch_data
from load import load_csv_to_postgres
from helpers import get_client

#get clickhouse client
client = get_client()

def main():
    '''
    
    '''

    # extract data
    fetch_data(client=client)

    # load data
    load_csv_to_postgres('tripdata.csv', 'tripdata')

    print('pipeline completed successfully')



if __name__ == '__main__':
    main()
import io
import pandas as pd

import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Add a data loader block and use Pandas to read data for the final quarter of 2020 (months 10, 11, 12).

    You can use the same datatypes and date parsing methods shown in the course.
    BONUS: load the final three months using a for loop and pd.concat

    """

    list_df = []
    for month in (10, 11, 12):
        print(f'Load month {month}')
        url = f'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-{month}.csv.gz'

        dates_cols = ["lpep_pickup_datetime", "lpep_dropoff_datetime"]

        dtypes = {
            'VendorID': pd.Int64Dtype(),
            'passenger_count': pd.Int64Dtype(),
            'trip_distance': float,
            'RatecodeID': pd.Int64Dtype(),
            'store_and_fwd_flag': str,
            'PULocationID': pd.Int64Dtype(),
            'DOLocationID': pd.Int64Dtype(),
            'payment_type': pd.Int64Dtype(),
            'fare_amount': float,
            'extra': float,
            'mta_tax': float,
            'tip_amount': float,
            'tolls_amount': float,
            'improvement_surcharge': float,
            'total_amount': float,
            'congestion_surcharge': float 
        }
        df = pd.read_csv(url, sep=',', dtype=dtypes, parse_dates=dates_cols)

        list_df.append(df)
    
    df = pd.concat(list_df)

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):
    """
    Add a transformer block and perform the following:

    Remove rows where the passenger count is equal to 0 and the trip distance is equal to zero.
    Create a new column lpep_pickup_date by converting lpep_pickup_datetime to a date.
    Rename columns in Camel Case to Snake Case, e.g. VendorID to vendor_id.
    Add three assertions:
        vendor_id is one of the existing values in the column (currently)
        passenger_count is greater than 0
        trip_distance is greater than 0

    """
    m0 = df['passenger_count'] > 0
    m1 = df['trip_distance'] > 0

    map_cols = {
        'VendorID': 'vendor_id',
        'RatecodeID': 'rate_code_id',
        'PULocationID': "pickup_location_id",
        'DOLocationID': 'drop_off_location_id',
    }
    df = df.loc[m0 & m1]
    df = (df
        .assign(lpep_pickup_date=df.lpep_pickup_datetime.dt.date)
        .rename(columns=map_cols)
    )
    print('Unique values of vandor_id column:', df['vendor_id'].unique())
    print('Number of unique dates is', df['lpep_pickup_date'].nunique())

    return df


@test
def test_output(df, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert df is not None, 'The output is undefined'


@test
def test_output1(df, *args) -> None:
    """
    vendor_id is one of the existing values in the column (currently)
    """
    assert 'vendor_id' in df.columns, 'vendor_id must be one of the existing values in the column'


@test
def test_output2(df, *args) -> None:
    """
    passenger_count is greater than 0
    """
    assert df['passenger_count'].min() > 0, 'passenger_count must be greater than 0'


@test
def test_output3(df, *args) -> None:
    """
    trip_distance is greater than 0
    """
    assert df['trip_distance'].min() > 0, 'trip_distance must be greater than 0'


from extract import extract_data

from transform import transform_data

from load import load_data



print("ETL Pipeline Started")



data = extract_data()



clean_data = transform_data(data)



load_data(clean_data)



print("ETL Pipeline Completed")
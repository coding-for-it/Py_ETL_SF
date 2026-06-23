import pandas as pd
import os

from src.logger import get_logger


logger = get_logger()



def extract_data():


    file_path = "data/sales.csv"


    if not os.path.exists(file_path):

        raise Exception("Sales file not found")



    logger.info(
        "Reading sales CSV file"
    )



    df = pd.read_csv(file_path)



    logger.info(

        f"Extracted {len(df)} records"

    )


    return df
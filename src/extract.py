import pandas as pd
import logging
import os


logger = logging.getLogger()



def extract_data():


    file_path = "data/sales.csv"


    try:


        logger.info("Extraction started")


        if not os.path.exists(file_path):

            raise FileNotFoundError(
                "Sales CSV file not found"
            )


        df = pd.read_csv(file_path)



        logger.info(

            f"{len(df)} records extracted"

        )


        print("Data Extracted")


        return df



    except Exception as e:


        logger.error(

            f"Extraction failed: {e}"

        )


        raise e
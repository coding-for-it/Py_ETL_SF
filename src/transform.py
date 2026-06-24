import logging


logger = logging.getLogger()



def transform_data(df):


    logger.info("Transformation started")


    try:


        # Missing value check

        missing = df.isnull().sum().sum()



        if missing > 0:


            logger.warning(

                f"{missing} missing values found"

            )


            df = df.fillna(0)



        else:


            logger.info(

                "No missing values found"

            )



        # Duplicate check


        duplicates = df.duplicated().sum()



        if duplicates > 0:


            logger.warning(

                f"{duplicates} duplicate rows removed"

            )


            df = df.drop_duplicates()



        else:


            logger.info(

                "No duplicates found"

            )



        # Data validation


        if df["ORDER_ID"].isnull().any():


            raise Exception(

                "ORDER_ID contains null values"

            )



        # Feature engineering


        df["TOTAL_SALES"] = (

            df["QUANTITY"]

            *

            df["PRICE"]

        )



        logger.info(

            "Transformation completed"

        )


        print("Data Transformed")


        return df



    except Exception as e:


        logger.error(

            f"Transformation failed: {e}"

        )


        raise e
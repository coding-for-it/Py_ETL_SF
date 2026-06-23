import logging


logging.basicConfig(

    filename="logs/etl.log",

    level=logging.INFO,

    format="%(asctime)s - %(levelname)s - %(message)s"

)



def transform_data(df):


    logging.info("Transformation started")

    print("Checking Data Quality...")



    # -------------------------
    # Data Quality Check 1
    # Missing values
    # -------------------------

    missing_values = df.isnull().sum().sum()


    print(
        "Missing values:",
        missing_values
    )


    if missing_values > 0:

        logging.warning(

            f"Dataset contains {missing_values} missing values"

        )


    else:

        logging.info(

            "No missing values found"

        )



    # -------------------------
    # Data Quality Check 2
    # Duplicate rows
    # -------------------------

    duplicates = df.duplicated().sum()


    print(

        "Duplicate records:",
        duplicates

    )


    if duplicates > 0:

        logging.warning(

            f"Found {duplicates} duplicate rows"

        )


    else:

        logging.info(

            "No duplicate records found"

        )



    # -------------------------
    # Remove duplicates
    # -------------------------

    df = df.drop_duplicates()



    logging.info(

        "Duplicate records removed"

    )



    # -------------------------
    # Handle missing values
    # -------------------------

    df = df.fillna(0)



    logging.info(

        "Missing values handled"

    )



    # -------------------------
    # Feature Engineering
    # Create TOTAL_SALES
    # -------------------------

    df["TOTAL_SALES"] = (

        df["QUANTITY"]

        *

        df["PRICE"]

    )



    logging.info(

        "TOTAL_SALES column created"

    )



    print(

        "Transformation completed"

    )



    logging.info(

        "Transformation completed successfully"

    )


    return df
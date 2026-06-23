import logging


from extract import extract_data

from transform import transform_data

from load import load_data



logging.basicConfig(

    filename="logs/etl.log",

    level=logging.INFO,

    format="%(asctime)s - %(levelname)s - %(message)s"

)



try:


    logging.info(
        "ETL Pipeline Started"
    )


    print(
        "ETL Pipeline Started"
    )



    # Extract

    data = extract_data()



    # Transform

    clean_data = transform_data(data)



    # Load

    load_data(clean_data)



    logging.info(

        "ETL Pipeline Completed Successfully"

    )


    print(

        "ETL Pipeline Completed"

    )



except Exception as e:


    logging.error(

        f"Pipeline failed: {e}"

    )


    print(e)
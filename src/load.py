import logging

from db import get_connection



logging.basicConfig(

    filename="logs/etl.log",

    level=logging.INFO,

    format="%(asctime)s - %(levelname)s - %(message)s"

)




def load_data(df):


    logging.info(
        "Loading process started"
    )



    conn = get_connection()


    cursor = conn.cursor()



    try:


        for index,row in df.iterrows():


            query = """

            INSERT INTO SALES

            (
            ORDER_ID,
            CUSTOMER_NAME,
            PRODUCT,
            QUANTITY,
            PRICE,
            ORDER_DATE,
            TOTAL_SALES
            )


            VALUES

            (%s,%s,%s,%s,%s,%s,%s)

            """



            cursor.execute(

                query,

                (

                int(row["ORDER_ID"]),

                row["CUSTOMER_NAME"],

                row["PRODUCT"],

                int(row["QUANTITY"]),

                float(row["PRICE"]),

                row["ORDER_DATE"],

                float(row["TOTAL_SALES"])

                )

            )



        conn.commit()



        logging.info(

            "Data loaded into Snowflake successfully"

        )


        print(
            "Data Loaded Into Snowflake"
        )



    except Exception as e:


        logging.error(

            f"Loading failed: {e}"

        )


        raise e



    finally:


        cursor.close()

        conn.close()
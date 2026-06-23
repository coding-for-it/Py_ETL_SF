import logging

from src.db import get_connection


logger = logging.getLogger()



def load_data(df):


    conn = get_connection()

    cursor = conn.cursor()



    try:


        for _, row in df.iterrows():


            query = """

            INSERT INTO SALES

            VALUES

            (%s,%s,%s,%s,%s,%s,%s)

            """



            cursor.execute(

                query,

                (

                row.ORDER_ID,

                row.CUSTOMER_NAME,

                row.PRODUCT,

                row.QUANTITY,

                row.PRICE,

                row.ORDER_DATE,

                row.TOTAL_SALES

                )

            )



        conn.commit()



        logger.info(

            f"{len(df)} records loaded into Snowflake"

        )



        print(
            "Data Loaded Successfully"
        )



    except Exception as e:


        logger.error(e)

        raise e



    finally:


        cursor.close()

        conn.close()
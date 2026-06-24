import logging

from src.db import get_connection



logger = logging.getLogger()



def load_data(df):


    conn = None

    cursor = None


    try:


        logger.info(

            "Loading started"

        )


        conn = get_connection()


        cursor = conn.cursor()



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



        for _, row in df.iterrows():



            cursor.execute(

                query,

                (

                row["ORDER_ID"],

                row["CUSTOMER_NAME"],

                row["PRODUCT"],

                row["QUANTITY"],

                row["PRICE"],

                row["ORDER_DATE"],

                row["TOTAL_SALES"]

                )

            )



        conn.commit()



        logger.info(

            f"{len(df)} records loaded successfully"

        )



        print(

            "Data Loaded Successfully"

        )



    except Exception as e:



        if conn:

            conn.rollback()



        logger.error(e)


        raise e



    finally:



        if cursor:

            cursor.close()



        if conn:

            conn.close()
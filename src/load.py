
from db import get_connection



def load_data(df):


    conn = get_connection()


    cursor = conn.cursor()


    for index,row in df.iterrows():


        sql = f"""

        INSERT INTO SALES

        VALUES

        (

        {row.ORDER_ID},

        '{row.CUSTOMER_NAME}',

        '{row.PRODUCT}',

        {row.QUANTITY},

        {row.PRICE},

        '{row.ORDER_DATE}',

        {row.TOTAL_SALES}

        )

        """


        cursor.execute(sql)



    print("Data Loaded Into Snowflake")



    cursor.close()

    conn.close()
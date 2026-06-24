import pandas as pd

from src.transform import transform_data



def test_total_sales_creation():


    data = {


        "ORDER_ID":[1],

        "CUSTOMER_NAME":["Test"],

        "PRODUCT":["Laptop"],

        "QUANTITY":[2],

        "PRICE":[50000],

        "ORDER_DATE":["2025-01-01"]

    }


    df = pd.DataFrame(data)


    result = transform_data(df)



    assert "TOTAL_SALES" in result.columns


    assert result["TOTAL_SALES"].iloc[0] == 100000

def transform_data(df):


    # remove duplicates

    df = df.drop_duplicates()


    # handle missing values

    df = df.fillna(0)


    # create total sales

    df["TOTAL_SALES"] = (
        df["QUANTITY"] *
        df["PRICE"]
    )


    print("Data Transformed")


    return df
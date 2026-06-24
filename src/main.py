from src.extract import extract_data

from src.transform import transform_data

from src.load import load_data

from src.logger import get_logger



logger = get_logger()



def run_pipeline():


    try:


        logger.info(

            "ETL Pipeline Started"

        )


        print(

            "ETL Pipeline Started"

        )



        data = extract_data()



        clean_data = transform_data(data)



        load_data(clean_data)



        logger.info(

            "ETL Pipeline Completed"

        )



        print(

            "ETL Pipeline Completed"

        )



    except Exception as e:



        logger.error(e)


        print(

            "Pipeline Failed:",

            e

        )





if __name__ == "__main__":


    run_pipeline()
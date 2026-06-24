from src.db import get_connection



def test_snowflake_connection():


    conn = get_connection()


    assert conn is not None


    conn.close()
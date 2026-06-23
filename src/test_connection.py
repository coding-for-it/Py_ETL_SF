from db import get_connection


conn = get_connection()


print("Snowflake Connected Successfully")


conn.close()
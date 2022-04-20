#!/usr/bin/env /opt/homebrew/anaconda3/bin/python 

import snowflake.connector

conn = snowflake.connector.connect(
                user='kevinluzbetak',
                password='password',
                account='account',
                warehouse='COMPUTE_WH',
                database='WEATHER'
                )

cur = conn.cursor()

SQL1 = """
DESCRIBE TABLE SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER
"""

SQL2 = """
SELECT * 
FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER
LIMIT 25;
"""

cur.execute(SQL2)
# print(cur.fetchone()[0])
result = cur.fetchall()

for i in result:
    if 'FURNITURE' in i:	
        print(i)





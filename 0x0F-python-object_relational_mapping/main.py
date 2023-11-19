#!/usr/bin/python3
from sqlalchemy import create_engine, MetaData, select

engine = create_engine('mysql://root:root@localhost/mydata')
try:
    conn = engine.connect()
    print('Connected')

    metadata = MetaData()
    metadata.reflect(bind=engine)
    for table in metadata.tables.keys():
        print(table)

except Exception as e:
    print(f'Error: {e}')

finally:
    if 'connection' in locals() and connection is not None:
        conn.close()
        print('Connection closed.')

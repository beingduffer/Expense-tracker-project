

conn=create_connection()
cursor=conn.cursor()
cursor.execute("""drop table expenses""")
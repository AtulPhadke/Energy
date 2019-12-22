import sqlite3

conn = sqlite3.connect('plantdata.db')

c = conn.cursor()

c.execute("""CREATE TABLE plantdata (
            bool text,
            time text,
            place text,
            plantname text,
            humidity real,
            temperature real,
            wateranalog real
            )""")
conn.commit()
conn.close()

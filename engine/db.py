import sqlite3


conn = sqlite3.connect("tasker.db")

curs = conn.cursor()

curs.execute("""CREATE TABLE user
    (email TEXT NOT NULL,
    password BLOB NOT NULL,
    id INT NOT NULL UNIQUE)
""")

conn.commit()
curs.execute("""CREATE TABLE tasks
    (task_name TEXT NOT NULL,
    user_id INT NOT NULL,
    id INT NOT NULL UNIQUE)
""")
conn.close()
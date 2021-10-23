import sqlite3
from datetime import datetime, date

conn = sqlite3.connect("log_db.sqlite",detect_types=sqlite3.PARSE_DECLTYPES) 
conn.execute("CREATE TABLE logs (id integer primary key, message text, [timestamp] timestamp)")
conn.execute("INSERT INTO logs(message, timestamp) values (?, ?)", ("message: error",'2012-12-25 23:59:59'))
conn.execute("INSERT INTO logs(message, timestamp) values (?, ?)", ("message: ok", datetime.now()))
conn.commit()datetime.now()
cur = conn.cursor()
cur.execute("SELECT * FROM logs")
print (cur.fetchone())
print (cur.fetchone())
conn.close()














	''''conn = sqlite3.connect('diary.db') 
	with conn:
		c = conn.cursor()
		unix = int(time.time())
		date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d'))
		c.execute("INSERT INTO diary(entry, datestamp) VALUES (?,?)",(entry1, date,))
		conn.commit()'
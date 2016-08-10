from flask import Flask
import sqlite3

app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Hello, World!'

def delete_table(table_name):
	conn = sqlite3.connect('happy_architecture.db')
	order_db = conn.cursor()
	order_db.execute('''DROP TABLE ''' + table_name)
	conn.commit()
	conn.close()

def clear_table(table_name):
	conn = sqlite3.connect('happy_architecture.db')
	order_db = conn.cursor()
	order_db.execute('''DELETE FROM'''+ table_name)
	conn.commit()
	conn.close()

def create_database():
	#clear database for testing
	delete_table("INDIVID_ORDERS")
	delete_table("ORDER_ITEMS")
	#create the database
	conn = sqlite3.connect('happy_architecture.db')
	order_db = conn.cursor()
	print "Opened database successfully"
	order_db.execute('''CREATE TABLE INDIVID_ORDERS
	       (ORDER_NUMBER INT PRIMARY KEY     NOT NULL,
	       TODAYS_DATE           DATE    NOT NULL,
	       NAME            INT     NOT NULL,
	       PHONE        TEXT NOT NULL,
	       EMAIL        TEXT NOT NULL);''')
	conn.commit()
	conn.close()

	conn = sqlite3.connect('happy_architecture.db')
	order_db = conn.cursor()
	order_db.execute('''CREATE TABLE ORDER_ITEMS
	       (ORDER_NUMBER INT PRIMARY KEY     NOT NULL,
	       UNIQUE_ID          TEXT    NOT NULL,
	       ITEM            TEXT     NOT NULL,
	       QUANTITY        INT NOT NULL,
	       PRICE        TEXT NOT NULL,
	       SUBTOTAL TEXT NOT NULL);''')
	conn.commit()
	conn.close()
	print "Tables created successfully";

	#print the tables
	conn = sqlite3.connect('happy_architecture.db')
	order_db = conn.cursor()
	order_db.execute('''SELECT name FROM sqlite_master WHERE type='table';''')
	print (order_db.fetchall())
	conn.commit()
	conn.close()


if __name__ == "__main__":
	create_database()
	app.run(debug=True, threaded=True, port=5000)

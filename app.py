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
	order_db.execute('''DELETE FROM '''+ table_name)
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

def insert_order(order_num, date, name, phone, email):
	conn = sqlite3.connect('happy_architecture.db')
	order_db = conn.cursor()
	order_db.execute('''INSERT INTO INDIVID_ORDERS(order_number, todays_date, name, phone, email)
						VALUES(?,?,?,?,?);''',(order_num,date,name,phone,email))
	conn.commit()

	print order_db.execute('''SELECT * FROM INDIVID_ORDERS''').fetchall()
	conn.commit()
	conn.close()

if __name__ == "__main__":
	clear_table('INDIVID_ORDERS')
	insert_order(1235, 8/10/2016, 'Lucy', '9082083212', 'shopper@gmail.com')
	app.run(debug=True, threaded=True, port=5000)

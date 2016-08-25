from flask import *
import sqlite3

app = Flask(__name__)


@app.route('/sign-in')
@app.route('/')
def hello_world():
    return render_template('sign-in.html')

@app.route('/sign-up')
def signup():
    return render_template('sign-up.html')

@app.route('/account-locked')
def accountlocked():
    return render_template('account-locked.html')

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
	conn.close()

def insert_order_items(order_num, unique_id, item_name, quantity, price):
	conn = sqlite3.connect('happy_architecture.db')
	order_db = conn.cursor()
	order_db.execute('''INSERT INTO ORDER_ITEMS(order_number, unique_id, ITEM, quantity, price, subtotal)
						VALUES(?,?,?,?,?,?);''',(order_num,unique_id,item_name,quantity,price, float(price)*quantity))
	conn.commit()
	conn.close()

def create_table_relationships():
	conn = sqlite3.connect('happy_architecture.db')
	order_db = conn.cursor()
	print order_db.execute('''SELECT NAME, TODAYS_DATE, ITEM FROM INDIVID_ORDERS CROSS JOIN ORDER_ITEMS;''').fetchall()
	conn.commit()
	conn.close()

def print_all_tables():
	conn = sqlite3.connect('happy_architecture.db')
	order_db = conn.cursor()
	print order_db.execute('''PRAGMA table_info(INDIVID_ORDERS)''').fetchall()
	conn.commit()
	print order_db.execute('''SELECT * FROM INDIVID_ORDERS''').fetchall()
	conn.commit()
	print order_db.execute('''SELECT * FROM ORDER_ITEMS''').fetchall()
	conn.commit()
	conn.close()


if __name__ == "__main__":
	clear_table('INDIVID_ORDERS')
	clear_table('ORDER_ITEMS')
	insert_order(1235, '2016-08-10', 'Lucy', '9082083212', 'shopper@gmail.com')
	insert_order_items(1235, '8y734z','apple',5,'0.5')
	print_all_tables()
	create_table_relationships()
	app.run(host="0.0.0.0", port="33")
	#app.run(debug=True, threaded=True, port=5000)

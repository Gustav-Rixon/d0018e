#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import random
from datetime import date

app = Flask(__name__)

#Intialize MySQL
mysql = MySQL(app)

app.secret_key = 'qwertyuiopå'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'qwertyuiopå'
app.config['MYSQL_DB'] = 'd0018e'

@app.route('/')
def index():
	return render_template('index.html')

#This is the url: http://130.240.200.45/Flask/login
@app.route("/login", methods=['GET', 'POST'])
def login():
	msg = ''
	# Check if "username" and "password" POST requests exist (user submitted form)
	if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
		# Create variables for easy access
		email = request.form['email']
		password = request.form['password']
		# Check if account exists using MySQL
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM Customers WHERE email = % s AND password = % s AND customer_id', (email, password,))
		# Fetch one record and return result
		account = cursor.fetchone()
		# If account exists in accounts table in out database
		if account:
			# Create session data, we can access this data in other routes
			session['loggedin'] = True
			session['password'] = account['password']
			session['email'] = account['email']
			# Redirect to home page

			return redirect(url_for('home'))
		else:
			msg = "you didn't say the magic word"
	return render_template('login.html', msg=msg)

@app.route('/logout')
def logout():
	session.pop('loggedin', None)
	session.pop('id', None)
	session.pop('username', None)
	return redirect(url_for('login'))

@app.route('/register', methods =['GET', 'POST'])
def register():
	msg = ''
	# Check if "username" and "password" POST requests exist (user submitted form)
	if request.method == 'POST' and 'first_name' in request.form and 'last_name' in request.form and 'password' in request.form and 'email' in request.form:
		first_name = request.form['first_name']
		last_name = request.form['last_name']
		password = request.form['password']
		email = request.form['email']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM Customers WHERE email = % s', (email, ))
		account = cursor.fetchone()
		if account:
			msg = 'Account alredy exists !'
		elif not first_name or not last_name or not password or not email:
			msg = 'Please fill out the form !'
		else:
			cursor.execute('INSERT INTO Customers VALUES (% s, % s, % s, % s, % s, % s)', (random.randrange(10000), first_name, last_name, password, email, 1, ))
			mysql.connection.commit()
			msg = 'You have successfully registered !'

	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('register.html', msg = msg) 

@app.route('/home')
def home():
	if 'loggedin' in session:
		return render_template('home.html', email=session['email'])
	return redirect(url_for('login'))

#This will be the profile page, only accessible for loggedin users
@app.route('/profile')
def profile():
	if 'loggedin' in session:
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM Customers WHERE email = % s', (session['email'],))
		account = cursor.fetchone()
		return render_template('profile.html', account=account)
	return redirect(url_for('login'))

@app.route('/shop')
def shop():
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
	cursor.execute('SELECT * FROM Products')
	prodData = cursor.fetchall()
	return render_template('shop.html', prodData=prodData)

@app.route('/cart')
def cart():
	if 'loggedin' not in session:
		return redirect(url_for('login'))

	else:
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT customer_id FROM Customers WHERE email = % s', (session['email'],))
		cusData = cursor.fetchone()
		cursor.execute('SELECT * FROM Products, Order_items, Orders WHERE customer_id = % s and order_item_id = order_id AND Order_items.prod_id = Products.prod_id', (cusData["customer_id"], ))
		ordData = cursor.fetchall()

	return render_template('cart.html', ordData=ordData)

@app.route('/addToCart', methods =['GET', 'POST'])
def addToCart():
	if 'loggedin' not in session:
		return redirect(url_for('login'))

	else:
		prod_id = request.args.get('productId')
		quy = request.args.get('quantityId')
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute("SELECT customer_id FROM Customers WHERE email = '" + session['email'] + "'")
		userId = cursor.fetchone()

		cursor.execute('SELECT * FROM Products WHERE prod_id = % s', (prod_id))
		prodData = cursor.fetchone()

		try:
			tmp = random.randrange(10000)
			val = tmp
			tmp2 = random.randrange(10000)
			cursor.execute('INSERT INTO Orders VALUES (% s,% s,% s,% s,% s,% s)', (tmp, 0, prod_id, None, 1, userId["customer_id"], ))
			mysql.connection.commit()

			cursor.execute('SELECT order_id FROM Orders WHERE order_id = % s', (val, ))
			orderInfo = cursor.fetchone()

			cursor.execute('INSERT INTO Order_items VALUES (% s,% s,% s)', (orderInfo["order_id"], 1, prodData["prod_id"], ))

			mysql.connection.commit()
			msg = "Added successfully"

		except:
			mysql.connection.rollback()
			msg = "Error occured"

	return redirect(url_for('cart'))

@app.route("/removeFromCart")
def removeFromCart():
	if 'email' not in session:
        	return redirect(url_for('login'))

	else:
		orderId = request.args.get('orderId')
		email = session['email']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

		try:
			cursor.execute("DELETE FROM Order_items WHERE order_item_id = % s", (orderId, ))
			cursor.execute("DELETE FROM Orders WHERE order_id = % s", (orderId, ))
			mysql.connection.commit()
			msg = "Added successfully"

		except:
			mysql.connection.rollback()
			msg = "Error occured"

	return redirect(url_for('cart'))

@app.route("/productDescription")
def productDescription():
	prod_id = request.args.get('productId')
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
	cursor.execute('SELECT * FROM Products WHERE prod_id = % s', (prod_id), )
	productData = cursor.fetchone()
	cursor.execute('SELECT stock FROM RelOwnProd WHERE prod_id = % s', (prod_id), )
	relOwnData = cursor.fetchone()
	cursor.execute('SELECT * FROM Feedback WHERE prod_id = % s', (prod_id))
	feedbackData = cursor.fetchall()

	return render_template('productDescription.html', data = productData, data2 = relOwnData, data3 = feedbackData)

@app.route("/checkout", methods=['GET','POST'])
def checkout():
	if 'loggedin' not in session:
		return redirect(url_for('login'))

	else:
		orderId = request.args.get('orderId')
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

		try:
			cursor.execute('SELECT * FROM Order_items WHERE order_item_id = % s', (orderId, ))
			orderInfo = cursor.fetchone()
			cursor.execute('SELECT stock FROM RelOwnProd WHERE prod_id = % s', (orderInfo["prod_id"], ))
			stockInfo = cursor.fetchone()

			if stockInfo["stock"] > orderInfo["order_item_quantity"]:
				newstock = stockInfo["stock"] - orderInfo["order_item_quantity"]

			cursor.execute('SELECT price FROM Products WHERE prod_id = % s', (orderInfo["prod_id"], ))
			proInfo = cursor.fetchone()
			cursor.execute('UPDATE RelOwnProd SET stock = % s WHERE prod_id = % s', (newstock, orderInfo["prod_id"], ))
			cursor.execute("DELETE FROM Order_items WHERE order_item_id = % s", (orderId, ))
			cursor.execute("UPDATE Orders SET order_status = 1, pris_fast = % s, quantity = % s WHERE order_id = % s", (proInfo["price"], orderInfo["order_item_quantity"], orderInfo["order_item_id"], ))
			mysql.connection.commit()
			msg = "Added successfully"

		except:
			mysql.connection.rollback()
			msg = "Error occured"

	return render_template('checkout.html', orderInfo=orderInfo, orderId=orderId)

@app.route("/vieworders", methods=['GET','POST'])
def vieworders():
	if 'loggedin' not in session:
		return redirect(url_for('login'))

	else:
		email = session['email']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT customer_id FROM Customers WHERE email = % s', (session['email'],))
		userId = cursor.fetchone()
		cursor.execute('SELECT Products.prod_name, Products.img_url, Products.prod_description, Orders.quantity, Orders.pris_fast, Orders.order_id, Orders.customer_id FROM Products, Orders WHERE order_status = 1 AND Orders.customer_id = % s AND Orders.prod_id = Products.prod_id', (userId["customer_id"], ))
		data = cursor.fetchall()

	return render_template("vieworders.html", data=data)

@app.route("/addComment", methods=['POST'])
def addComment():
	if 'loggedin' not in session:
		return redirect(url_for('login'))

	else:
		email = session['email']
		comment = request.form['comment']
		grade = request.form['grade']
		data = request.form['data']
		today = date.today()
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT customer_id FROM Customers WHERE email = % s', (email, ))
		userId = cursor.fetchone()
		try:
			sql = "INSERT INTO Feedback (prod_id, rating, comment, date, customer_id) VALUES (%s, %s, %s, %s, %s)"
			val = (data, grade, comment, today, userId["customer_id"])
			cursor.execute(sql, val)
			mysql.connection.commit()
			msg = 'Added successfully'

		except:
			mysql.connection.rollback()
			msg = "Error occured"

	return productDescription()

@app.route("/changeQty", methods=['POST'])
def changeQty():

	ammount = request.form['amount']
	orderId = request.form['orderId']
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

	try:
		cursor.execute("UPDATE Order_items SET order_item_quantity = % s WHERE order_item_id = % s", (ammount, orderId ))
		mysql.connection.commit()
		msg = 'Added successfully'

	except:
		mysql.connection.rollback()
		msg = "Error occured"

	return redirect(url_for('cart'))

####Admin code is here########

@app.route("/admin", methods=['GET', 'POST'])
def admin():
	msg = ''
	# Check if "username" and "password" POST requests exist (user submitted form)
	if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
		# Create variables for easy access
		email = request.form['email']
		password = request.form['password']
		# Check if account exists using MySQL
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM Owner WHERE email = % s AND password = % s AND owner_id', (email, password,))
		# Fetch one record and return result
		account = cursor.fetchone()
		# If account exists in accounts table in out database
		if account:
			# Create session data, we can access this data in other routes
			session['loggedin'] = True
			session['password'] = account['password']
			session['email'] = account['email']
			# Redirect to home page

			return render_template('adminHome.html')
		else:
			msg = "you didn't say the magic word"
	return render_template('adminLogin.html', msg=msg)

@app.route("/adminProducts")
def adminProducts():
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
	cursor.execute('SELECT * FROM Products')
	prodData = cursor.fetchall()
	return render_template('adminProducts.html', prodData=prodData)

@app.route("/productDescriptionAdmin")
def productDescriptionAdmin():
	prod_id = request.args.get('productId')
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
	cursor.execute('SELECT * FROM Products WHERE prod_id = % s', (prod_id))
	productData = cursor.fetchone()
	cursor.execute('SELECT stock FROM RelOwnProd WHERE prod_id = % s', (prod_id))
	relOwnData = cursor.fetchone()
	cursor.execute('SELECT * FROM Feedback WHERE prod_id = % s', (prod_id))
	feedbackData = cursor.fetchall()

	return render_template('productDescriptionAdmin.html', data = productData, data2 = relOwnData, data3 = feedbackData)

@app.route("/viewCustomers")
def viewCustomers():
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
	cursor.execute('SELECT first_name, last_name, email FROM Customers WHERE owner_id = 1')
	data = cursor.fetchall()

	return render_template('viewCustomers.html', data=data)

@app.route("/addProduct", methods=['GET', 'POST'])
def addProduct():
	name = request.form['name']
	price = request.form['price']
	pic = request.form['pic']
	category = request.form['category']
	description = request.form['description']
	stock = request.form['stock']
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

	try:
		cursor.execute('SELECT MAX(rel_own_prod_id) FROM RelOwnProd')
		Id = cursor.fetchone()
		Id = Id["MAX(rel_own_prod_id)"] + 1

		cursor.execute('INSERT INTO RelOwnProd (owner_id, prod_id, stock) VALUES (% s, % s, % s)', (1, Id, stock), )
		cursor.execute('INSERT INTO Products (prod_id, prod_name, price, img_url, categorie_id, prod_description) VALUES (% s, % s, % s, % s, % s, % s)', (Id, name, price, pic, category, description), )
		mysql.connection.commit()
		msg = 'Added successfully'
	except:
		mysql.connection.rollback()
		msg = "Error occured"

	return redirect(url_for('adminTools'))

@app.route("/removeProduct", methods=['GET', 'POST'])
def removeProduct():
	ID = request.form['ID']
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

	try:
		cursor.execute('DELETE From RelOwnProd WHERE prod_id = % s', (ID, ))
		mysql.connection.commit()
		msg = 'Added successfully'

	except:
		mysql.connection.rollback()
		msg = "Error occured"

	return redirect(url_for('adminTools'))


@app.route("/removeComment", methods=['GET', 'POST'])
def removeComment():
	comment = request.args.get('productComment')
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

	try:
		cursor.execute('DELETE From Feedback WHERE feedback = % s', (comment, ))
		mysql.connection.commit()
		msg = 'Added successfully'

	except:
		mysql.connection.rollback()
		msg = "Error occured"


	return redirect(url_for('adminProducts'))

@app.route("/addCategory", methods=['GET', 'POST'])
def addCategory():
	add = request.form['nameCat']
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

	try:
		cursor.execute('INSERT INTO Categories (category_id, category_name) VALUES (% s, % s)', (random.randrange(1000000), add, ))
		mysql.connection.commit()
		msg = 'Added successfully'

	except:
		mysql.connection.rollback()
		msg = "Error occured"

	return redirect(url_for('adminTools'))

@app.route("/removeCategory", methods=['GET', 'POST'])
def removeCategory():
	rem = request.form['nameCat2']
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

	try:
		cursor.execute('DELETE From Categories WHERE category_id = % s', (rem, ))
		mysql.connection.commit()
		msg = 'Added successfully'

	except:
		mysql.connection.rollback()
		msg = "Error occured"


	return redirect(url_for('adminTools'))

@app.route("/modifyStock", methods=['GET', 'POST'])
def modifyStock():
	prod = request.args.get('productId')
	data = request.form['newStock']
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

	try:
		cursor.execute('UPDATE RelOwnProd SET stock = % s WHERE prod_id = % s', (data, prod, ))
		mysql.connection.commit()
		msg = 'Added successfully'

	except:
		mysql.connection.rollback()
		msg = "Error occured"

	return redirect(url_for('adminProducts'))

@app.route("/modifyPrice", methods=['GET', 'POST'])
def modifyPrice():
	prod = request.args.get('productId')
	data = request.form['newPrice']
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

	try:
		cursor.execute('UPDATE Products SET price = % s WHERE prod_id = % s', (data, prod, ))
		mysql.connection.commit()
		msg = 'Added successfully'

	except:
		mysql.connection.rollback()
		msg = "Error occured"

	return redirect(url_for('adminProducts'))

@app.route("/changePicture", methods=['GET', 'POST'])
def changePicture():
	prod = request.args.get('productId')
	data = request.form['newPic']
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

	try:
		cursor.execute('UPDATE Products SET img_url = % s WHERE prod_id = % s', (data, prod, ))
		mysql.connection.commit()
		msg = 'Added successfully'

	except:
		mysql.connection.rollback()
		msg = "Error occured"

	return redirect(url_for('adminProducts'))

@app.route("/changeName", methods=['GET', 'POST'])
def changeName():
	prod = request.args.get('productId')
	data = request.form['newName']
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

	try:
		cursor.execute('UPDATE Products SET prod_name = % s WHERE prod_id = % s', (data, prod, ))
		mysql.connection.commit()
		msg = 'Added successfully'

	except:
		mysql.connection.rollback()
		msg = "Error occured"

	return redirect(url_for('adminProducts'))

@app.route("/viewCustomerOrder", methods=['GET', 'POST'])
def viewCustomerOrder():
	email = request.args.get('customer')
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
	cursor.execute('SELECT customer_id FROM Customers WHERE email = % s', (email, ))
	userId = cursor.fetchone()

	cursor.execute('SELECT Products.prod_name, Products.img_url, Products.prod_description, Orders.quantity, Orders.pris_fast, Orders.order_id, Orders.customer_id FROM Products, Orders WHERE order_status = 1 AND Orders.customer_id = % s AND Orders.prod_id = Products.prod_id', (userId["customer_id"], ))
	data = cursor.fetchall()

	return render_template("viewordersAdmin.html", data=data, userId=userId)

@app.route("/adminTools", methods=['GET', 'POST'])
def adminTools():
	return render_template('adminTools.html')


if __name__ == "__main__":
	app.run()

#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import random

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
	#cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
	#prod = request.form['prod_id']
	#print (prod)
	return render_template('cart.html')
#def addToCart():
#def removeFromCart():

@app.route("/productDescription")
def productDescription():
	prod_id = request.form['prod_id']
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
	cursor.execute('SELECT * FROM Products WHERE prod_id = ' + prod_id)
	productData = cursor.fetchall()
	return render_template('productDescription.html')

if __name__ == "__main__":
	app.run()


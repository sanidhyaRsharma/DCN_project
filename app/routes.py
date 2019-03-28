from flask import render_template, flash, url_for, redirect, request, session
from app import app, mysql
from app.forms import LoginForm
from functools import wraps
import time
import string

HOST='127.0.0.1'
PORT=1234


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first")
            return redirect(url_for('login'))
    return wrap

@app.route('/', methods = ['GET','POST'])
@app.route('/login', methods = ['GET','POST'])
def login():
	form = LoginForm()
	# s.bind((HOST,PORT))
	# s.listen(1)				#Listen for a connection
	# incoming_socket, address = s.accept()
	# sendData1 = "Login detected at" + time.strftime("%a, %d %b %Y %H:%M:%S %Z")
	# print(sendData1)
	# stringAddress= str(address)

	if form.validate_on_submit():
		username = form.username.data
		password = form.password.data
		cursor = mysql.connect().cursor()
		cursor.execute("SELECT * FROM Employees WHERE username='"+username+"' AND password_hash='"+password+"'")
		data = cursor.fetchone()
		if data is not None:
			session['logged_in'] = True
			session['username'] = username
			# return """<h1>Login Successful</h1>"""
			return redirect(url_for('home'))
		else:
			sendData1 = "This is the Organization's SMTP MAIL Service, <br> Login detected at " + time.strftime("%a, %d %b %Y %H:%M:%S %Z")
			sendData2 = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

			return """<h1>Username or Password is incorrect!</h1><br>
					<a href= "/login" >Login</a><br><br>
					"""+sendData1+"""
					<br>
					Intruder IP = """+ sendData2+"""
					<br>
					"""
	return render_template('login.html', form = form)

@app.route('/home')
@login_required
def home():
	d = [{'details':"Closing report for FY-17",'month':'December-2017'},
		 {'details':"Remuneration for employees", 'month':'January-2018'},
		 {'details':"Sanction for logistical upgrades",'month':'February-2018'},
		 {'details':"Budget for FY-18", 'month':'March-2018'},
		 {'details':"Permission for workshop",'month':'April-2018'}]
	return render_template('home.html', d = d, username = session['username'])

@login_required
@app.route('/logout/')
def logout():
	session.clear()
	return redirect(url_for('login'))
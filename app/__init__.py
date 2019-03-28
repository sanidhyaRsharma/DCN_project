from flask import Flask
from config import Config
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__, static_url_path = '/templates')
app.config.from_object(Config)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'PassWord234'
app.config['MYSQL_DATABASE_DB'] = 'EmployeeData'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

from app import routes
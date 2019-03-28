import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'It_is_a_secret'
	SQL_ALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql://161080032:161080032@localhost:1234/payroll'

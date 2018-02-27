import cx_Oracle

def run(host, port, timeout=2):
	username = "admin"
	password = "123"
	dbname = 1
	dsn = cx_Oracle.makedsn(host, port, dbname)
	print dsn
	connection = cx_Oracle.connect(username, password, dsn)


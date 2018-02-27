import pymssql

USERNAME = ('sa',)


def run(host, port, timeout=1):
    for username in USERNAME:
        for password in PASSWORD:
            try:
                pymssql.connect(host=host, port=int(
                    port), user=username, password=password, timeout=0, login_timeout=timeout)
                return "MSSQL weak password. useranem: %s, password: %s " % (username, password)
            except Exception as e:
            	# print e.args[0][0]
            	pass

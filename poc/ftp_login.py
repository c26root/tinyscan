import ftplib

USERNAME = ('ftp', 'www', 'admin', 'root', 'db', 'wwwroot', 'data', 'web', )


def run(ip, port, timeout=2):

    if 'ftp' not in PASSWORD:
        PASSWORD.insert(0, 'ftp')

    for username in USERNAME:
        for password in PASSWORD:
            password = str(password.replace('{user}', username))
            try:
                ftp = ftplib.FTP()
                ftp.timeout = timeout
                ftp.connect(ip, port)
                ftp.login(username, password)
                if password == '':
                    password = "null"
                if username == 'ftp' and password == 'ftp':
                    return "ftp anonymous login"
                return "ftp weak password. username: %s, password: %s" % (username, password)
            except Exception, e:
                # print e
                pass

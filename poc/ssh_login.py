import paramiko
# paramiko.util.logging.getLogger('paramiko.transport').addHandler(paramiko.util.logging.NullHandler())
paramiko.util.logging.getLogger('paramiko.transport').disabled = True

USERNAME = ('root', 'admin', 'ftp', 'oracle', 'weblogic', )


def run(ip, port, timeout=5):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for username in USERNAME:
        for password in PASSWORD:
            password = str(password.replace('{user}', username))
            try:
                ssh.connect(ip, port, username, password, timeout=timeout,
                            allow_agent=False, look_for_keys=False)
                ssh.exec_command('whoami', timeout=timeout)
                if password == '':
                    password = "null"
                return "SSH weak password. username: %s, password: %s" % (username, password)
            except Exception, e:
                if "Unable to connect" in e or "timed out" in e:
                    return
            finally:
                ssh.close()

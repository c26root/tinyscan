from vnclib import VNC


PASSWORD = ("", "123", "123456", "admin", "test", )


def run(ip, port, timeout=5):
    for password in PASSWORD:
        try:
            v = VNC()
            v.connect(ip, port, timeout)
            code, msg = v.login(password)
            if code == 0:
                return "VNC weak password. password: %s" % password
        except Exception as e:
            if 'No authentication required' in str(e):
                return "No authentication required"
            # print e
    return False


if __name__ == '__main__':
    print run("10.0.0.1", 5900)


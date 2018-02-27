import socket


def run(ip, port, timeout=2):
    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, int(port)))
        s.send("INFO\r\n")
        result = s.recv(1024)
        if "redis_version" in result:
            return "Redis unauthorized"
        elif "Authentication" in result:
            for password in PASSWORD:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, int(port)))
                s.send("AUTH %s\r\n" % (password))
                result = s.recv(1024)
                if '+OK' in result:
                    return u"Redis weak password. password: %s" % (password)
    except Exception, e:
        # print e
        pass
    finally:
        s.close()


import socket


def run(ip, port, timeout=5):
    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, int(port)))
        flag = "envi"
        # envi
        # dump
        # reqs
        # ruok
        # stat
        s.send(flag)
        data = s.recv(1024)
        s.close()
        if 'Environment' in data:
            return u"Zookeeper Unauthorized access"
    except:
        pass

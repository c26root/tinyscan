import socket

def run(ip, port, timeout=5):
    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, int(port)))
        s.send("stats\r\n")
        result = s.recv(1024)
        if "STAT version" in result:
            return "Memcache unauthorized"
    except Exception, e:
        pass


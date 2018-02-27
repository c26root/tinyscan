import socket
from smb.SMBConnection import SMBConnection


def ip2hostname(ip):
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        return hostname
    except:
        pass
    try:
        query_data = "\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x20\x43\x4b\x41\x41" + \
                     "\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41" + \
                     "\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x00\x00\x21\x00\x01"
        dport = 137
        _s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        _s.sendto(query_data, (ip, dport))
        x = _s.recvfrom(1024)
        tmp = x[0][57:]
        hostname = tmp.split("\x00", 2)[0].strip()
        hostname = hostname.split()[0]
        return hostname
    except:
        pass

USERNAME = ('administrator', 'admin', 'test', )


def run(ip, port, timeout=5):
    socket.setdefaulttimeout(timeout)
    hostname = ip2hostname(ip)

    if 'anonymous' not in PASSWORD:
        PASSWORD.insert(0, 'anonymous')
    if not hostname:
        return
    for username in USERNAME:
        for password in PASSWORD:
            try:
                password = str(password.replace('{user}', username))
                conn = SMBConnection(username, password, 'xunfeng', hostname)
                if conn.connect(ip) == True:
                    if password == 'anonymous':
                        return "SMB anonymous share"
                    return "SMB weak password. username: %s, password: %s" % (username, password)
            except Exception, e:
                if "Errno 10061" in str(e) or "timed out" in str(e):
                    return

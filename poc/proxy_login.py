import requests


def run(ip, port, timeout=3):

    PROXIES = ("HTTP", "SOCKS4", "SOCKS5", )
    URL = 'http://2017.ip138.com/ic.asp'
    result = []

    for protocol in PROXIES:
        proxies = {
            "http": "%s://%s:%d/" % (protocol, ip, port),
            "https": "%s://%s:%d/" % (protocol, ip, port),
        }
        try:
            r = requests.get(URL, proxies=proxies, timeout=timeout)
            if 'content-type' in r.content:
                result.append("%s Proxy" % protocol)
        except Exception as e:
            # print e
            pass

    return result

# print run('127.0.0.1', 8888)
# print run('127.0.0.1', 8080)
# print run('192.168.117.128', 8080)

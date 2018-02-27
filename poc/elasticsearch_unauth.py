import requests


def run(url, timeout=5):
    try:
        r = requests.get(url + '/_cat', timeout=timeout, verify=False)
        if "/_cat/master" in r.content:
            return "ElasticSearch unauth"
    except Exception as e:
        print e
        pass

if __name__ == '__main__':
    print run("http://127.0.0.1:9200")

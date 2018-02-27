def load_dic(path):
    with open(path) as f:
        return [i.strip() for i in f]


def load_target(path):
    with open(path) as f:
        s = json.load(f)
    return s


def load_host(path):
    with open(path) as f:
        return [i.strip() for i in f]
import os

DEFAULT_HTTPLIB_TIMEOUT = 2
DEBUG = False
POC_DIR = "poc"
DICT_DIR = os.path.join(os.path.dirname(__file__), "dict")
TOP100_PASSWORD_DICT_PATH = os.path.join(DICT_DIR, "top100.txt")
SMALL_PASSWORD_DICT_PATH = os.path.join(DICT_DIR, "small.txt")
COMPONENT_PLUGIN_INFO = {
    "tomcat": ["CVE-2017-12615", "tomcat_manage_login"],
    "jenkins": ["jenkins_command"],
}
SERVER_PLUGIN_INFO = {
    # "21": ["ftp_login"],
    # "22": ["ssh_login"],
    # "135": ["smb_login"],
    "445": ["ms17-010"],
    # "1080": ["proxy_login"],
    # "1433": ["mssql_login"],
    # "2181": ["zookeeper_unauth"],
    # "3306": ["mysql_login"],
    # "5432": ["postgresql_login"],

    # "5900": ["vnc_login"],
    # "5901": ["vnc_login"],
    # "5902": ["vnc_login"],

    # "6379": ["redis_login"],
    # "8080": ["proxy_login"],
    # "11211": ["memcache_unauth"],
    # "27017": ["mongodb_login"],
}
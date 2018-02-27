#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import sys
import json
import time
import httplib
import logging
import urlparse
import requests
import gevent
from gevent import socket, monkey, pool
from lib.terminaltables import AsciiTable, SingleTable
from common import load_dic, load_host, load_target
from config import DEFAULT_HTTPLIB_TIMEOUT, POC_DIR, DEBUG
from config import TOP100_PASSWORD_DICT_PATH, SMALL_PASSWORD_DICT_PATH
from config import SERVER_PLUGIN_INFO, COMPONENT_PLUGIN_INFO

TOP100_PASSWORD_DICT = load_dic(TOP100_PASSWORD_DICT_PATH)
SMALL_PASSWORD_DICT = load_dic(SMALL_PASSWORD_DICT_PATH)

requests.packages.urllib3.disable_warnings()
monkey.patch_all()

httplib.socket.setdefaulttimeout(DEFAULT_HTTPLIB_TIMEOUT)
sys.path.append(POC_DIR)
pool = pool.Pool(10)
data = [("Plugin", "Host", "Response")]

if DEBUG:
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',)


def print_logo():
    print '''
 _________  ___  ________       ___    ___ 
|\___   ___\\  \|\   ___  \    |\  \  /  /|
\|___ \  \_\ \  \ \  \\ \  \   \ \  \/  / /
     \ \  \ \ \  \ \  \\ \  \   \ \    / / 
      \ \  \ \ \  \ \  \\ \  \   \/  /  /  
       \ \__\ \ \__\ \__\\ \__\__/  / /    
        \|__|  \|__|\|__| \|__|\___/ /     
                              \|___|/      
                                           '''


def _import(poc):
    poc = __import__(poc)
    # 添加默认字典
    if not getattr(poc, "PASSWORD", ""):
        setattr(poc, "PASSWORD", SMALL_PASSWORD_DICT[:])
    setattr(poc, "SMALL_PASSWORD_DICT", SMALL_PASSWORD_DICT[:])
    setattr(poc, "TOP100_PASSWORD_DICT", TOP100_PASSWORD_DICT[:])
    setattr(poc, "DEBUG", DEBUG)
    return poc


def get_info_by_ip(ip):
    import sadb
    rate, empl_uid = 0, ""
    ipinfo = sadb.getipinfo(ip)
    if ipinfo:
        rate = ipinfo["rate"]
        empl_uid = ipinfo["empl_uid"]
    return rate, empl_uid


def run_task(plugin, *args):
    if plugin not in sys.modules:
        logging.info("import plugin: %s" % plugin)
        # poc = _import(plugin)
        sys.modules[plugin] = _import(plugin)
    poc = sys.modules[plugin]
    if poc:
        host, port = args
        result = poc.run(host, port)
        if result:
            # rate, empl_uid = get_info_by_ip(host)
            print "[%s] %s %s" % (plugin.center(15, ' '), ("%s:%s" % (host, port)).ljust(21), result)
            # print "[%s] %s %s %s" % (plugin.center(15, ' '), ("%s %s" %
            # (rate, empl_uid)).center(26, ' '), ("%s:%s" % (host,
            # port)).ljust(21), result)
            data.append([plugin, "%s:%s" % (host, port), result])


def scanhost():
    path = r'C:\Users\Administrator\Desktop\go\portscan\10.2.txt'
    hosts = load_host(path)

    def find_plugins_by_name(search):
        for name, plugins in SERVER_PLUGIN_INFO.iteritems():
            if search == name:
                return plugins
        return False

    for i in hosts:
        host, port_str = i.split(":")
        port = int(port_str)
        plugins = find_plugins_by_name(port_str)
        if plugins:
            for plugin in plugins:
                pool.spawn(run_task, plugin, host, port)

    pool.join()


def scanurl():
    hosts = load_target()

    def find_plugins_by_name(search):
        for name, plugins in COMPONENT_PLUGIN_INFO.iteritems():
            if name in search:
                return plugins
        return False

    for i in hosts:
        url, server, title = i['url'], i['server'], i['title'].lower()
        parse = urlparse.urlparse(url)
        port = 80
        l = parse.netloc.split(':')
        if len(l) == 2:
            host, port = l
            port = int(port)
        else:
            host = l[0]

        plugins = find_plugins_by_name(title)
        if plugins:
            for plugin in plugins:
                pool.spawn(run_task, plugin, host, port)

    pool.join()


def show_result(data):
    table = AsciiTable(data)
    # table.inner_row_border = True
    print table.table

if __name__ == '__main__':

    # print_logo()
    scanhost()
    # scanurl()
    show_result(data)

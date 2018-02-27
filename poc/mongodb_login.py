import socket
import binascii

def run(ip, port, timeout=5):
    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, int(port)))
        data = binascii.a2b_hex(
            "3a000000a741000000000000d40700000000000061646d696e2e24636d640000000000ffffffff130000001069736d6173746572000100000000")
        s.send(data)
        result = s.recv(1024)
        if "ismaster" in result:
            getlog_data = binascii.a2b_hex(
                "480000000200000000000000d40700000000000061646d696e2e24636d6400000000000100000021000000026765744c6f670010000000737461727475705761726e696e67730000")
            s.send(getlog_data)
            result = s.recv(1024)
            if "totalLinesWritten" in result:
                return "MongoDB unauthorized"
    except Exception, e:
        # print e
        pass

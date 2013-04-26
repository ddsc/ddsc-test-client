# (c) Fugro GeoServices. MIT licensed, see LICENSE.rst.
import socket
import time
import settings

SOCKS_SETTINGS = settings.SOCKS

def main():
    host = SOCKS_SETTINGS['host']
    port = SOCKS_SETTINGS['port']
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    timeout = SOCKS_SETTINGS['timeout']
    s.settimeout(timeout)
	file_loc = SOCKS_SETTINGS['test_file_dst']

    try:
        s.connect((host, port))
        print 'connected'
        i = 1
        with open(file_loc, 'r') as f:
            reader = f.readline()
            while reader:
                try:
                    s.send(reader)
                    s.recv(3)
                    time.sleep(1)
                except Exception, e:
                    print 'send error'
                    print e
                    return
                try:
                    reader = f.readline()
                    print i
                    print reader
                    time.sleep(0.1)
                    i += 1
                except:
                    print 'reader error'
            print 'final row:' + reader
            f.close()
        print 'file complete'
        s.close()
    except socket.error:
        print 'error: connection timeout'
        exit()

main()

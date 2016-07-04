#!/usr/bin/python
import optparse
from socket import *


def saveFile(msg):
    f = open('a.txt', 'rw')
    f.write(msg)
    f.close()


def connScan(host, port):
    try:
        client = socket(AF_INET, SOCK_STREAM)
        client.connect((host, port))
        msg = "[+]%d tcp open" % port
        saveFile(msg)
        client.close()
    except Exception, e:
        # print(e.message + "\n")
        print("[-]%d tcp closed" % port)


def portScan(host, ports):
    # try:
    #     targetIp = gethostbyname(host)
    # except:
    #     print("[-] can't resolve %s : Unknown host" % (host))
    #     return
    #
    # try:
    #     targetName = gethostbyaddr(targetIp)
    #     print("[+] Scan Results0 for: " + targetName[0])
    # except:
    #     print("[+] Scan Results1 for: " + targetIp)

    setdefaulttimeout(10)
    for tgtPort in ports:
        print("\n----Scaning port %s------" % tgtPort)
        connScan(host, int(tgtPort))


def main():
    print "hello,world!"
    parser = optparse.OptionParser('usage %prog -H <tartget host> -p <tartget port>')
    parser.add_option('-H', dest='targetHost', type='string', help='specify target host')
    parser.add_option('-p', dest='targetPort', type='string', help='specify target port')
    (options, args) = parser.parse_args()
    targetHost = options.targetHost
    targetPorts = str(options.targetPort).split(', ')
    print(targetPorts)
    if targetHost == None:
        print parser.usage
        exit(0)

    for item in targetPorts:
        print(item)

    portScan(targetHost, targetPorts)

def main2():
    parser = optparse.OptionParser('usage %prog -H <tartget host> ')
    parser.add_option('-H', dest='targetHost', type='string', help='specify target host')
    (options, args) = parser.parse_args()
    ip = options.targetHost

    if ip == None:
        print parser.usage
        exit(0)

    ports = xrange(12250, 12259)
    portScan(ip, ports)

if __name__ == '__main__':
    main2()



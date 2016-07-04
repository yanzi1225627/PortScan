#-*- coding:utf-8 -*---
#!/usr/bin/python
import paramiko
import time
import threading
import threadpool


def saveFile(msg, clear = False):
    if(clear == False):
        f = open('a.txt', 'a') #追加写文件
    else:
        f = open('a.txt', 'w') #清空文件
    f.write(msg)
    f.close()


def getTime():
    curr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return curr


def ssh2(ip, port, username, passwd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port, username, passwd, timeout=5)
        print("ssh..." )
    except paramiko.AuthenticationException, e:
        msg = "   ssh login port may be %i" % port
        saveFile("\n" + getTime() + msg)
        print(("---port = %i AuthenticationException = " + e.message + "---") % (port))
        saveFile("end scan at = " + getTime())
        exit(0)
    except paramiko.BadHostKeyException, e:
        print("BadHostKeyException = " + e.hostname)
    except paramiko.SSHException, e:
        print("SSHException = " + e.message)
    except Exception, e:
        print("%d fail" % port)

def main():
    username = 'root'
    passwd = 'test'
    ip = '45.32.33.**'
    ports = xrange(10000, 12259)
    saveFile("start scan at = " + getTime(), True)
    i = 0
    for port in ports:
        t = threading.Thread(target=ssh2, args=(ip, port, username, passwd))
        i+=1
        print "\n %i \n" % i
        # t.start()
        # ssh2(ip, port, username, passwd)

if __name__ == '__main__':
    main()


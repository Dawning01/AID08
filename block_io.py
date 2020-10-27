"""
非阻塞IO实例
"""
import select

from socket import *
from time import sleep ,ctime

log=open("my.log","a")
s=socket(AF_INET,SOCK_STREAM)
s.bind(("0.0.0.0",8888))
s.listen(5)
# 设置为非阻塞
s.setblocking(False)
# s.settimeout(1)
while True:
    try:
        c,addr = s.accept()
        print("Connect from ",addr)
    except timeout as e:
        print("发生超时")
    # except BlockingIOError as e:
        # print("干点别的")
        print("开始写日志")
        sleep(2)
        msg="%s : %s\n"%(ctime(),e)
        print(msg)
        log.write(msg)
        log.flush()
    except BlockingIOError as e:
        print("非阻塞日志")
        sleep(2)
    else:
        data = c.recv(1024)
        print(data.decode())
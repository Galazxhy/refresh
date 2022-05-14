import threading
import requests
import codecs
from tqdm import tqdm
import random
import time

def main():
    # 获取代理header和ip
    header = head()
    ip = ipProxies()

    # 获取目标URL，随机访问一篇博客
    url = getURL()

    # 访问URL
    return askURL(url,header,ip)

def ipProxies():
    f = codecs.open("IP.txt", "r+", encoding="utf-8")
    ip = f.readlines()
    f.close()
    IP = {'http':random.choice(ip)[-2::-1][::-1]}
    print("本次使用IP(proxies)为：",IP['http'])
    return IP

def head():
    f = codecs.open("User-Agent.txt","r+",encoding="utf-8")
    head = f.readlines()
    f.close()
    header = {"User-Agent":random.choice(head)[-3::-1][::-1]}
    print("本次使用header(User-Agent)为：", header["User-Agent"])
    return header

def getURL():
    f = codecs.open("url.txt","r+",encoding="utf-8")
    URL = f.readlines()
    f.close()
    url = random.choice(URL)[-2::-1][::-1]
    print("本次使用访问的链接为：", url)
    return url

def askURL(url,header,ip):
    try:
        request = requests.get(url=url,headers=header,proxies=ip)
        print(request)
        time.sleep(5)
    except:
        print("本次访问失败!")

class refresh_thread(threading.Thread):
    def __init__(self, thread_name):
        super(refresh_thread, self).__init__(name = thread_name)

    def run(self):
        print("%s正在运行中......" % self.name)


def thread_fun():
    num = 0
    while 1:
        print("访问")
        main()

if __name__ == '__main__':
    for i in range(15):
        t = threading.Thread(target=thread_fun)
        t.start()

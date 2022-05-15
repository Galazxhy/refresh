import threading
import requests
import codecs
from tqdm import tqdm
import random
import time

def main(i):
    # 获取代理header和ip
    header = head()
    ip = ipProxies()

    # 获取目标URL，随机访问一篇博客
    url = getURL()

    # 访问URL
    return askURL(i,url,header,ip)

def ipProxies():
    f = codecs.open("IP.txt", "r+", encoding="utf-8")
    ip = f.readlines()
    f.close()
    IP = {'http':random.choice(ip)[-2::-1][::-1]}
    # print("本次使用IP(proxies)为：",IP['http'])
    return IP

def head():
    f = codecs.open("User-Agent.txt","r+",encoding="utf-8")
    head = f.readlines()
    f.close()
    header = {"User-Agent":random.choice(head)[-3::-1][::-1]}
    # print("本次使用header(User-Agent)为：", header["User-Agent"])
    return header

def getURL():
    f = codecs.open("url.txt","r+",encoding="utf-8")
    URL = f.readlines()
    f.close()
    url = random.choice(URL)[-2::-1][::-1]
    # print("本次使用访问的链接为：", url)
    return url

def askURL(i,url,header,ip):
    try:
        request = requests.get(url=url,headers=header,proxies=ip)
        print("thread:{}".format(i),request)
        time.sleep(5)
    except:
        print("")
        # print("本次访问失败!")

def thread_fun(i):
    while 1:
        print("thread:{} 访问".format(i))
        main(i)

if __name__ == '__main__':
    thread_num = int(input("输入线程数量(建议为15)："))
    for i in range(thread_num):
        t = threading.Thread(target=thread_fun, args=(i,))
        t.start()

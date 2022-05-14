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

if __name__ == '__main__':
    while True:
        num = 30
        for num in tqdm(range(num), desc="正在访问", ncols=70):
            print("这是第" + str(num + 1) + "次访问")
            main()
        print("------one cycle end-----")
        time.sleep(5)


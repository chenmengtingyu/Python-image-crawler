import urllib.request
import time
import re
import os


def getHtmlCode(url):
    # 避免反爬虫
    headers = {
        'User-Agent': 'Mozilla/5.0(Linux; Android 6.0; Nexus 5 Build/MRA58N) \
    AppleWebKit/537.36(KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'
    }
    url = urllib.request.Request(url, headers=headers)
    page = urllib.request.urlopen(url).read()
    page = page.decode('UTF-8')
    return page


def getImage(page):
    imageList = re.findall(r'(https:[^\s]*?(jpg|png|gif|jfif))"', page)
    x = 0

    path = input('请输入保存路径(格式为E:/image):')
    if not os.path.exists(path):
        os.mkdir(path)

    for imageUrl in imageList:
        startTime = time.time()
        try:
            print('正在下载: %s' % imageUrl[0])
            image_save_path = path + '/%d.png' % x
            urllib.request.urlretrieve(imageUrl[0], image_save_path)
            x = x + 1
        except:
            continue
        endTime = time.time()
        print('下载完成,耗时%.2f秒' % (endTime - startTime))
    pass


if __name__ == '__main__':
    url = input('请输入网站:')
    page = getHtmlCode(url)
    getImage(page)

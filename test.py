# from PIL import Image
# from imageshi import run
import requests


data = str("撒打飞机")

url = 'https://www.baidu.com/s?cl=3&wd={}'.format(data)


req = requests.get(url, verify=False)
print(req.text)


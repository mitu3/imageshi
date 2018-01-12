from cutimage import cuti
import requests
import base64
import urllib.parse
from gettoken import get_token

token = get_token()
header = {'Content-Type':'application/x-www-form-urlencoded'}
host = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic'
params = {'access_token':token }
cuti()
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


image = get_file_content('test.png')
def basicGeneral(image):
    data = {}
    data['image'] = base64.b64encode(image).decode()
    return data

data = basicGeneral(image)



def run():
    req = requests.post(host, data=data, headers=header, params=params, verify=False)

    return req.json()['words_result'][0]['words']

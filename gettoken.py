
import urllib.request
import json



def get_token():
    apiKey = 'ul1WRFay6crwDXDGbSrsGI4w'
    secretKey = 'pBUY0dKrutFLVRNBjOmvLKnnmufZDBvL'
    aurh_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(apiKey,secretKey)
    print(aurh_url)
    res = urllib.request.urlopen(aurh_url)
    json_data = res.read()
    print(json_data)
    print(type(json_data))
    return json.loads(str(json_data,encoding='utf-8'))['access_token']



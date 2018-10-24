import requests
import json

headers =   {
                'cache-control': 'no-cache',
                'content-type':'application/json',
                'x-api-key':'8fd881d8-a61b-438c-a458-f8d72eb36a10',
                'x-clientId':'42e19814-209f-46f8-bda5-fbb85ffcb54d'
            }

data =  {
            "url":"",
            "method":"GET",
            "location":"all"
        }

bungeeUrl = 'https://www.bungeetech.com/api/v1/crawl/'

def crawlUrl(url):
    global data,bungeeUrl
    data['url'] = url
    response = requests.post(bungeeUrl,data=json.dumps(data),headers=headers)
    return response

inputRequest = {}
inputRequest['url'] = "https://www.bedbathandbeyond.com/store/category/gifts/gifts-by-interest/fitness-health-gifts/14830?ml=v2&icid=gift_promo17"
response = crawlUrl(inputRequest['url'])
print(response.status_code)
print(response.text)
file = open('testfile.txt','w')
 
file.write(response.text)
file.close()

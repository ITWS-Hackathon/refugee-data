import requests
import json
headers = {'Bearer': 'AAAAAAAAAAAAAAAAAAAAACouawEAAAAAHRlgxSjjVR9Kgf3VmMp89FoHSao%3D8kmNQUznpGbHWsrqkitxgAaYjzSBI2qZvUo3va2jifj0ZwwWwI'}
# req= requests.get("https://api.twitter.com/2/tweets/search/recent?query=cat%20has%3Amedia%20-grumpy&tweet.fields=created_at&max_results=100", headers)
# response= req.json()
# dataResponse= json.load(response) (read json file and save it to dataResponse)
f= open('AfricansinUkraine.json')
dataResponse= json.load(f)
print(dataResponse)
a = "AfricansinUkraine"
i = 1

for item in dataResponse["data"]:
    b = a + str(i) + '.json'
    
    with open(b, 'w') as g:

        json.dump(item, g)
    #print(item['data']['id'])
    #print(item)
    i += 1
f.close()
# print(response)
    

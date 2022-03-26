import requests
import json
headers = {'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAACouawEAAAAAHRlgxSjjVR9Kgf3VmMp89FoHSao%3D8kmNQUznpGbHWsrqkitxgAaYjzSBI2qZvUo3va2jifj0ZwwWwI'}
req= requests.get("https://api.twitter.com/2/tweets/search/recent?query=%23AfricansinUkraine&max_results=100&until_id=1507670246093590529", headers=headers)
response= req.json()
#json.dump(response, 'AfricansinUkraineMax.json')
#dataResponse= json.load(response)
#f= open('AfricansinUkraineMax.json')
#print(response)
a = "AfricansinUkraineSecondBatch"
i = 1

for item in response["data"]:
    b = a + str(i) + '.json'
    
    with open(b, 'w') as g:

        json.dump(item, g)
    i += 1
    

import requests
import json
headers = {'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAACouawEAAAAAHRlgxSjjVR9Kgf3VmMp89FoHSao%3D8kmNQUznpGbHWsrqkitxgAaYjzSBI2qZvUo3va2jifj0ZwwWwI'}
req= requests.get("https://api.twitter.com/2/tweets/search/recent?query=%23AfricansinUkraine&max_results=100&until_id=1507670246093590529", headers=headers)
response= req.json()
# saving all tweets to AfricansinUkraine.json files. w= write, += creates if file doesn't exist, or replaces file if file exists
f= open('AfricansinUkraine.json', "w+")
json.dump(response, f)
print(f.read())
# print(response)

# Saving objects in AfricansinUkraine into their own json files
a = "AfricansinUkraine"
i = 1

for item in response["data"]:
    b = a + str(i) + '.json'
    
    with open(b, 'w') as g:

        json.dump(item, g)
    i += 1
    

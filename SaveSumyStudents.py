import requests
import json
headers = {'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAACouawEAAAAAHRlgxSjjVR9Kgf3VmMp89FoHSao%3D8kmNQUznpGbHWsrqkitxgAaYjzSBI2qZvUo3va2jifj0ZwwWwI'}
req= requests.get("https://api.twitter.com/2/tweets/search/recent?query=%23SaveSumyStudents&max_results=100", headers=headers)
response= req.json()
# saving all tweets to SaveSumyStudents.json files. w= write, += creates if file doesn't exist, or replaces file if file exists
f= open('SaveSumyStudents.json', "w+")
json.dump(response, f)
print(f.read())
print(response)

# Saving objects in SaveSumyStudents into their own json files
a = "SaveSumyStudents"
i = 1

for item in response["data"]:
    b = a + str(i) + '.json'
    
    with open(b, 'w') as g:

        json.dump(item, g)
    i += 1
    

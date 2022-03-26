import requests
import json
import pandas as pd
headers = {'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAACouawEAAAAAHRlgxSjjVR9Kgf3VmMp89FoHSao%3D8kmNQUznpGbHWsrqkitxgAaYjzSBI2qZvUo3va2jifj0ZwwWwI'}
req= requests.get("https://api.twitter.com/2/tweets/search/recent?query=%23AfricansinUkraine&max_results=100&until_id=1507670246093590529", headers=headers)
response= req.json()

# file = open("test.json", "w")
# file.write(response)
# file.close()
# print(type(response))
# print(response)

df = pd.DataFrame.from_dict(response['data']) 
print(df)
df.to_csv (r'test.csv', index = False, header=True)

# print(response)
# pandas.json_to_csv(response)
# pdObj = pd.read_json(response)
# print(pdObj)
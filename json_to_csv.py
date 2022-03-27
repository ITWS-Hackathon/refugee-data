# import requests
# import json
# import pandas as pd
# headers = {'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAACouawEAAAAAHRlgxSjjVR9Kgf3VmMp89FoHSao%3D8kmNQUznpGbHWsrqkitxgAaYjzSBI2qZvUo3va2jifj0ZwwWwI'}
# req= requests.get("https://api.twitter.com/2/tweets/search/recent?query=%23AfricansinUkraine&max_results=100&until_id=1507670246093590529", headers=headers)
# response= req.json()

# print(response)


# file = open("data/AfricansinPoland.json", "r")
# content = file.read()
# json_content = json.loads(content)
# df = pd.DataFrame.from_dict(json_content['data'])
# print(df)
# df.to_csv(r'test2.csv', index=False, header=True)

# # file.write(response)
# # file.close()
# # print(type(response))
# # print(response)

# # df = pd.DataFrame.from_dict(response['data']) 
# # print(df)
# # df.to_csv (r'test.csv', index = False, header=True)

# # print(response)
# # pandas.json_to_csv(response)
# # pdObj = pd.read_json(response)
# # print(pdObj)

import plotly.express as px

df = px.data.gapminder().query("continent == 'Oceania'")
fig = px.bar(df, x='year', y='pop',
             hover_data=['lifeExp', 'gdpPercap'], color='country',
             labels={'pop':'population of Canada'}, height=400)
fig.show()
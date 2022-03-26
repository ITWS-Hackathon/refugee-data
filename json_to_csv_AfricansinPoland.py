import pandas as pd
import json

file = open("data/AfricansinPoland.json", "r")
content = file.read()
json_content = json.loads(content)
df = pd.DataFrame.from_dict(json_content['data'])
print(df)
df.to_csv(r'AfricansinPoland.csv', index=False, header=True)
# pdObj_dict= json.loads(pdObj)
# csvData= pdObj.to_csv('AfricansinPoland.csv', index=False)
# df = pd.DataFrame.from_dict(pdObj['data']) 
# print(df)
# print(csvData)
import pandas as pd
import json

file = open("data/SaveSumyStudents.json", "r")
content = file.read()
json_content = json.loads(content)
df = pd.DataFrame.from_dict(json_content['data'])
print(df)
df.to_csv(r'SaveSumyStudents.csv', index=False, header=True)

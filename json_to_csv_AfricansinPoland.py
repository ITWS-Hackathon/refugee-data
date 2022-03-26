import pandas as pd

df = pd.read_json (r'AfricansinPoland.json')
df.to_csv (r'AfricansinPoland.csv', index = None)
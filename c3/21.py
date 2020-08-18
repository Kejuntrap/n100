import pandas as pd

wiki = pd.read_json('jawiki-country.json', lines=True)
for i in range(len(wiki)):
    print(wiki['text'])

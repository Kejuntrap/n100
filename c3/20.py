import pandas as pd

wiki = pd.read_json('jawiki-country.json', lines=True)
uk = wiki[wiki['title'] == 'イギリス'].text.values
print(uk)
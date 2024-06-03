import pandas as pd

data = open('geo-reviews-dataset-2023.tskv', encoding='utf-8').read()
all_lines = []
for row in data.split('\n')[:-1]:
    row_array = row.split('\t')
    result = {arr.split('=')[0]: arr.split('=')[1] for arr in row_array}
    result['rating'] = float(result['rating'])
    all_lines.append(result)
df = pd.DataFrame(all_lines, columns=['address', 'name_ru', 'rating', 'rubrics', 'text'])
df.info()
df.to_csv('geo.csv', index=False)
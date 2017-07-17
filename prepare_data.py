# coding=utf-8
from datetime import datetime
import json
import pandas as pd
import numpy as np


with open('price_data.json', 'r') as f:
    price_list = json.load(f)


for i in xrange(0, len(price_list['data'])):
    dt = datetime.strptime(price_list['data'][i].get('time'), '%Y-%m-%dT%H:%M:%S.%fZ')
    price_list['data'][i]['time'] = datetime.strftime(dt, '%Y-%m-%d')


df = pd.DataFrame(price_list['data'])
# print df

group_data = df.groupby(by=['time'], as_index=False)
agg_group_data = group_data.agg({'usd': [np.mean, np.max, np.min]})

formatted_data = dict()
for i in xrange(0, len(agg_group_data)):
    formatted_data[agg_group_data.get('time')[i]] = dict()
    formatted_data[agg_group_data.get('time')[i]]['mean'] = agg_group_data.get('usd').get('mean')[i]
    formatted_data[agg_group_data.get('time')[i]]['max'] = agg_group_data.get('usd').get('amax')[i]
    formatted_data[agg_group_data.get('time')[i]]['min'] = agg_group_data.get('usd').get('amin')[i]

with open('formatted_data.json', 'w') as f:
    json.dump(formatted_data, f)







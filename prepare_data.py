# coding=utf-8

import json

with open('price_data', 'r') as f:
    data = json.load(f)

for price in data['data']:
    print price
from datetime import datetime, timedelta
import json

FIRST_BUYING_DATE = '2017-05-01'
FINAL_HISTORY_DATE = '2017-07-17'
BUYING_MONEY = 50
TOTAL_SPENT_MONEY = 0
NUM_OF_ETH = 0

USD_TO_TWD = 30
ETH_TO_TWD = 5200


with open('formatted_data.json', 'r') as f:
    data = json.load(f)

first_dt = datetime.strptime(FIRST_BUYING_DATE, '%Y-%m-%d')
current_dt = first_dt
final_dt = datetime.strptime(FINAL_HISTORY_DATE, '%Y-%m-%d')


week = 0
print current_dt, final_dt
while current_dt <= final_dt:
    print datetime.strftime(current_dt, '%Y-%m-%d')
    price = data.get(datetime.strftime(current_dt, '%Y-%m-%d')).get('mean')
    NUM_OF_ETH += BUYING_MONEY / price
    TOTAL_SPENT_MONEY += BUYING_MONEY
    current_dt += timedelta(days=7)
    week += 1
    print "I get {} eth at ${} on {}".format(str(BUYING_MONEY / price), price, datetime.strftime(current_dt, '%Y-%m-%d'))

print "===============REPORT================"
print "NUM OF BUYING: ", week
print "TOTAL_SPENT_MONEY: ", TOTAL_SPENT_MONEY, TOTAL_SPENT_MONEY * USD_TO_TWD
print "NUM_OF_ETH: ", NUM_OF_ETH, NUM_OF_ETH * ETH_TO_TWD
print "RATIO: ", (NUM_OF_ETH * ETH_TO_TWD) / (TOTAL_SPENT_MONEY * USD_TO_TWD)
print "====================================="
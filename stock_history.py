import tushare as ts, pandas as pd, os

#Please enter your token (minimum 120 credits required for this code)
pro = ts.pro_api("Please enter your own token hear: ")

#all the listed stocks' codes and list dates
listed_stocks = pro.stock_basic(exchange='', list_status='L', fields='ts_code, list_date')

#create a folder to store the daily data
if not os.path.exists("./history"):
    os.makedirs("./history")

#get the historical daily data of all listed stocks and store them in the history folder
for stock in listed_stocks.itertuples():
    ts_code = stock[1]
    print(f"Now retrieving {ts_code}'s historical daily data...")
    df = pro.daily(ts_code=ts_code, start_date=stock[2])
    df.to_csv(f"./history/{ts_code}.csv", encoding="utf-8-sig", index=False)

print("Finished!")

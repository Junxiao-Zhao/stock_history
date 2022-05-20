# stock_history
The purpose of of this code is to retrieve and store all the listed stocks' daily history for further analysis. In this code, we will retrieve the index data from Tushare for analyzing. Tushare is a free and open financial big data platform of all data categories. You can easily retrieve the data you want by simply a few lines of code, and do not need to worry about the integrality and the accuracy of the data, which will greatly improve the productivity and eliminate the need for data preprocessing.

If you would like to have a try, please register through the following link: https://tushare.pro/register?reg=456046.

Codes:

First, we need to import tushare and pandas (You can get your token from Profile-TOKEN and the index code from Data Api).

    import tushare as ts, pandas as pd, os
    
    pro = ts.pro_api("Please enter your token hear!")

Second, retrieve all the listed stocks's ts_code and list_date, which will be used to retrieve daily history of each stock later.

    listed_stocks = pro.stock_basic(exchange='', list_status='L', fields='ts_code, list_date')

Third, create a folder called "history" for storing the csv files (the the folder already existed, do nothing).

    if not os.path.exists("./history"):
        os.makedirs("./history")

Finally, retrieve each stocks' daily history, sort by the trade dates, store them in the csv files.

    for stock in listed_stocks.itertuples():
        ts_code = stock[1]
        print(f"Now retrieving {ts_code}'s historical daily data...")
        df = pro.daily(ts_code=ts_code, start_date=stock[2])
        #sort the trade date in ascending order
        df['trade_date'] = pd.to_datetime(df['trade_date'])
        df.sort_values("trade_date", ascending=True, inplace=True)
        #store in csv
        df.to_csv(f"./history/{ts_code}.csv", encoding="utf-8-sig", index=False)

    print("Finished!")

Results:

In the history folder:

<img width="502" alt="Screenshot 2022-05-20 143625" src="https://user-images.githubusercontent.com/78573538/169467858-2234e503-412a-4da9-acba-aa8effa58155.png">

In 000001.SZ.csv:

<img width="589" alt="Screenshot 2022-05-20 143733" src="https://user-images.githubusercontent.com/78573538/169468129-5e72ac60-cdba-4248-a752-352a16859df3.png">

P.S.

Next code will be automatically update the daily history every day.

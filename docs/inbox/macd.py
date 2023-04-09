import akshare as ak
import pandas as pd
import datetime

def get_data():
    # 获取当前日期
    today = datetime.date.today()
    end_date = today.strftime("%Y-%m-%d")

    # 计算五年前的日期
    start_date = (today - pd.DateOffset(years=5)).strftime("%Y-%m-%d")

    # 获取上证50指数数据
    sh50_df = ak.index_zh_stock_daily(symbol="sh000016", start_date=start_date, end_date=end_date)
    return sh50_df


def calculate_macd(data, short=12, long=26, signal=9):
    data = data.copy()
    data['ewm_short'] = data['close'].ewm(span=short).mean()
    data['ewm_long'] = data['close'].ewm(span=long).mean()

    data['dif'] = data['ewm_short'] - data['ewm_long']
    data['dea'] = data['dif'].ewm(span=signal).mean()
    data['macd'] = 2 * (data['dif'] - data['dea'])
    return data


if __name__ == '__main__':
    sh50_data = get_data()
    sh50_macd_data = calculate_macd(sh50_data)
    print(sh50_macd_data.tail())

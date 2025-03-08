import yfinance as yf
from tradingview_ta import TA_Handler, Interval


class analysis:
    def __init__(self, name):
        self.company_name = f'{name}.NS'
        self.yf_api_fetch = yf.Ticker(self.company_name)
        self.company_info = self.yf_api_fetch.info
        self.company_symbol = name
        self.tradingview_data = self.tradingview_connect(name)

    def tradingview_connect(self, symbol):
        handler = TA_Handler(
            symbol=symbol,
            screener="india",
            exchange="NSE",
            interval='1d'
        )
        analysis = handler.get_analysis()
        summary = analysis.summary
        oscillator  = analysis.oscillators
        indicators = analysis.indicators

        data = {
            "summery": summary,
            "oscillator": oscillator,
            "indicators": indicators
        }
        return data
   
    def share_price(self):
        return self.company_info['currentPrice']
    
    def share_price_range(self, period='max', interval='1d'):
        stock = self.yf_api_fetch
        share_price_arr = stock.history(period=period, interval=interval)
        if share_price_arr.empty : return []
        filtered_data = []    
        for index, row in share_price_arr.iterrows():
            date = index.strftime('%Y-%m-%d')
            share_price = round(row['Close'], 2)
            volume = row['Volume']
            filtered_data.append({
                'time': date,
                'share_price': share_price,
                'volume': volume
            })
        return filtered_data

    # using for company_section in webpage 
    def company_data(self):
        row_data_tradingview = self.tradingview_data['indicators']
        row_data_yfinance = self.yf_api_fetch.info
        data = {
            'share_price': row_data_yfinance['currentPrice'],
            'change':round(row_data_tradingview['change'], 2),
            'c_name':row_data_yfinance['shortName'],
            'c_symbol':row_data_yfinance['symbol'].split('.')[0]
        }
        return data


if __name__ == '__main__':
    company_name = "ITC"
    analys = analysis(company_name)

    print(analys.share_price_range('1mo', '1d'))
    
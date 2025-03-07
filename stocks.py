import twelvedata

client = twelvedata.TDClient(apikey="7daaa342d3f14c0ea42df0be7c78ecf8")

if __name__ == "__main__":
    while True:
        text = input("Get stock price: ").upper()
        try:
            stock_data = client.time_series(symbol=text, interval="1min", outputsize=1).as_json()
            print(f"Price of {text}: {stock_data[0]['close']}")
        except (KeyError, IndexError):
            print("Invalid stock symbol or no data available")
        except Exception as e:
            print(f"Error: {e}")
            


import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define the ticker symbol and time frame for analysis
ticker_symbol = "AAPL"
start_date = "2010-01-01"
end_date = "2022-03-30"

# Fetch the historical stock price data using the Yahoo Finance API
stock_data = yf.download(ticker_symbol, start_date, end_date)

# Compute basic statistics for the stock price data
mean_price = stock_data["Adj Close"].mean()
std_price = stock_data["Adj Close"].std()
max_price = stock_data["Adj Close"].max()
min_price = stock_data["Adj Close"].min()

# Print the basic statistics to the console
print("Basic Statistics for " + ticker_symbol + " Stock Price Data:")
print("Mean Price: $" + str(round(mean_price, 2)))
print("Standard Deviation: $" + str(round(std_price, 2)))
print("Maximum Price: $" + str(round(max_price, 2)))
print("Minimum Price: $" + str(round(min_price, 2)))

# Plot the stock price data using a line chart
sns.set_style("darkgrid")
plt.figure(figsize=(12, 6))
plt.plot(stock_data.index, stock_data["Adj Close"], color="blue")
plt.title("Historical Stock Prices for " + ticker_symbol)
plt.xlabel("Date")
plt.ylabel("Adjusted Close Price ($)")
plt.show()

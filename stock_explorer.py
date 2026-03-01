"""
Stock Data Explorer
A simple tool to download and visualize stock data
"""

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def main():
    print("=" * 50)
    print("STOCK DATA EXPLORER")
    print("=" * 50)
    
    # Get user input
    ticker = input("\nEnter stock ticker (e.g., AAPL, GOOGL, MSFT): ").upper()
    
    print(f"\nDownloading data for {ticker}...")
    
    # Download stock data for 2023
    try:
        data = yf.download(ticker, start="2023-01-01", end="2024-01-01", progress=False)
        
        if data.empty:
            print(f"Error: No data found for {ticker}")
            return
            
    except Exception as e:
        print(f"Error downloading data: {e}")
        return
    
    # Calculate basic statistics
    first_price = float(data['Close'].iloc[0])
    last_price = float(data['Close'].iloc[-1])
    highest_price = float(data['High'].max())
    lowest_price = float(data['Low'].min())
    
    # Calculate percentage change for the year
    year_change = ((last_price - first_price) / first_price) * 100
    
    # Display results
    print(f"\n{ticker} - 2023 Summary")
    print("-" * 50)
    print(f"Starting price (Jan 1):  ${first_price:.2f}")
    print(f"Ending price (Dec 31):   ${last_price:.2f}")
    print(f"Year change:             {year_change:+.2f}%")
    print(f"Highest price:           ${highest_price:.2f}")
    print(f"Lowest price:            ${lowest_price:.2f}")
    
    # Calculate daily returns
    data['Daily_Return'] = data['Close'].pct_change()
    avg_return = data['Daily_Return'].mean() * 100
    volatility = data['Daily_Return'].std() * 100
    
    print(f"\nAverage daily return:    {avg_return:.3f}%")
    print(f"Daily volatility:        {volatility:.3f}%")
    
    # Create visualization
    print(f"\nGenerating chart...")
    
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Close'], linewidth=2, color='blue')
    plt.title(f'{ticker} Stock Price - 2023', fontsize=16, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Price ($)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    # Save the chart
    filename = f'{ticker}_2023_chart.png'
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"✓ Chart saved as: {filename}")
    
    # Show the chart
    plt.show()
    
    print("\nDone!")

if __name__ == "__main__":
    main()
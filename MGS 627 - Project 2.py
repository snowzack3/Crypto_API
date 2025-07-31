# Import needed packages
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Fetch crypto data from api
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 50,
    'page': 1,
    'sparkline': 'false'
}

response = requests.get(url, params=params)
data = response.json()

# Step 2: Convert to DataFrame
df = pd.DataFrame(data)
df2 = df[['id','symbol', 'price_change_24h', 'price_change_percentage_24h']]

# Step 3: Convert DataFrame to CSV
df2.to_csv('crypto.csv', index=False)

# Step 4: Print max() of numeric column with an informative statement
max_prices = df2['price_change_percentage_24h'].max()
print('The highest price change by percentage in the last 24 hours is', max_prices, '%')

# Step 5: Create a DF with only the top 10 largest values
top10 = df.sort_values(by='price_change_percentage_24h', ascending=False).head(10)
df3 = pd.DataFrame(top10[['id', 'symbol', 'price_change_24h', 'price_change_percentage_24h']])

# Step 5: Plot the summary data (used matplotlib website to find more customization options for the graph)
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(top10['id'], top10['price_change_percentage_24h'], color='red')
ax.set_xlabel("Cryptocurrency", fontsize=14, fontweight='bold')
ax.set_ylabel("Percentage", fontsize=14, fontweight='bold')
ax.set_title("Top 10 price changes by percentage", fontsize=16, fontweight='bold')
ax.set_xticklabels(top10['id'], rotation=45, ha='right')
plt.tight_layout()
plt.show()

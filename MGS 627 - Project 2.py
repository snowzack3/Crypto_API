#    Web Scraping
#    MGS 627: Project 2

# We have learned a lot so far, now is a change to show it off!
# Demonstrate that you can pull data from the web and perform some
# summary statistics on it.

# When grading this project it is important to consider
# 1) Did you print the right outputs and your
#   code work.
# 2) Did you comment your code, so we understand what
#   you did.
# 3) The elegance of the solution (i.e. concise code instead
#   of extraneous code or outputs)

# Find an API to pull data from. Many of your favor sites have an API, but if
# you are having trouble finding one, here is a list of public:
# 'c'. Do not use any sources that we
# have gone over in class. While these are good examples, we have already gone over them.

# For this project, access the API and pull data.
# Turn this data into a pandas dataset with at least one numeric column and one text
# column. Then save that data as a csv file. Next, use that numeric column to calculate
# and print the max() of that column in an informative text statement. Create a dataframe
# that is only 10 largest values. Then plot this summary data similar to how we did
# in week 5's lab. This will be using the .hist or .plot # method of a pandas DataFrame.

# An example is a script using MarketStack API to pull stock prices over a month.
# The code would print 'The highest stock price of NKE was 80.94', and it would
# generate a graph of the top 10 stock prices over that month.

# Please include any API credentials required to run the code as this is how I will
# test if your query is successful.

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

import mysql.connector

# Connection details
config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Duke#7539',
    'database': 'stocks'
}

try:
    # Establish connection
    connection = mysql.connector.connect(**config)

    if connection.is_connected():
        print("Connection to MySQL database successful!")
        connection.close()
    else:
        print("Connection failed!")

except mysql.connector.Error as error:
    print("Error while connecting to MySQL", error)


import requests

# Replace 'YOUR_TOKEN_HERE' with your actual token
token = 'sk_973ce1ded0ff4efab9bd04fba84d7742'

# Example endpoint (replace with the specific endpoint you want to access)
endpoint = 'https://cloud.iexapis.com/stable/stock/AAPL/quote'

# Parameters (if any)
params = {
    'token': token
}

try:
    response = requests.get(endpoint, params=params)

    if response.status_code == 200:
        data = response.json()
        print("Data retrieved successfully:")
        print(data)
    else:
        print("Error:", response.status_code)
        print(response.text)

except requests.exceptions.RequestException as e:
    print("Request error:", e)


import requests

# Replace 'YOUR_TOKEN_HERE' with your actual token
token = 'sk_973ce1ded0ff4efab9bd04fba84d7742'

symbols = ['AAPL', 'TSLA', 'MSFT', 'NVDA', 'GOOGL', 'AMZN', 'FB', 'NFLX', 'PYPL', 'JPM', 'GS', 'DIS', 'CRM', 'BABA']
endpoint = 'https://cloud.iexapis.com/stable/stock/{}/quote'

for symbol in symbols:
    try:
        response = requests.get(endpoint.format(symbol), params={'token': token})

        if response.status_code == 200:
            data = response.json()
            print(f"Symbol: {data['symbol']}")
            print(f"Currency: {data['currency']}")
            print(f"Latest Price: {data['latestPrice']}")
            print(f"Change: {data['change']}")
            print(f"Change Percent: {data['changePercent']}")
            print("------")
        else:
            print(f"Error fetching data for {symbol}: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print("Request error:", e)


import requests
import mysql.connector

# API data retrieval function
def get_stock_data(symbol, token):
    endpoint = f'https://cloud.iexapis.com/stable/stock/{symbol}/quote'
    params = {'token': token}

    try:
        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching data for {symbol}: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print("Request error:", e)
        return None

# MySQL connection details
config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Duke#7539',
    'database': 'stocks'
}

# Stocks to fetch data for
symbols = ['AAPL', 'TSLA', 'MSFT', 'NVDA', 'GOOGL', 'AMZN', 'FB', 'NFLX', 'PYPL', 'JPM', 'GS', 'DIS', 'CRM', 'BABA']

# Establish MySQL connection
try:
    connection = mysql.connector.connect(**config)

    if connection.is_connected():
        print("Connection to MySQL database successful!")

        cursor = connection.cursor()

        # Creating a table if it doesn't exist
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS stock_data (
            id INT AUTO_INCREMENT PRIMARY KEY,
            symbol VARCHAR(10),
            currency VARCHAR(10),
            latest_price DECIMAL(10, 2),
            change_value DECIMAL(10, 2),
            change_percent DECIMAL(10, 2)
        )
        '''
        cursor.execute(create_table_query)
        connection.commit()

        # Fetching data from API and inserting into the table
        for symbol in symbols:
            stock_data = get_stock_data(symbol, 'sk_60acb782e5ab422eb86e9380ce4f5c0d')  # New IEX Cloud token

            if stock_data:
                insert_query = '''
                INSERT INTO stock_data (symbol, currency, latest_price, change_value, change_percent)
                VALUES (%s, %s, %s, %s, %s)
                '''
                values = (
                    stock_data['symbol'],
                    stock_data['currency'],
                    stock_data['latestPrice'],
                    stock_data['change'],
                    stock_data['changePercent']
                )
                cursor.execute(insert_query, values)
                connection.commit()

        print("Data inserted successfully!")

        cursor.close()
        connection.close()

    else:
        print("Connection failed!")

except mysql.connector.Error as error:
    print("Error while connecting to MySQL", error)


import mysql.connector

# MySQL connection details
config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Duke#7539',
    'database': 'stocks'
}

# Connect to MySQL
try:
    connection = mysql.connector.connect(**config)
    if connection.is_connected():
        cursor = connection.cursor()

        # Fetching all data from the stock_data table
        select_query = "SELECT * FROM stock_data"
        cursor.execute(select_query)
        data = cursor.fetchall()

        # Closing the database connection
        cursor.close()
        connection.close()

        if data:
            # Displaying all data
            for row in data:
                print(row)

        else:
            print("No data found in the stock_data table.")

    else:
        print("Connection failed!")

except mysql.connector.Error as error:
    print("Error while connecting to MySQL", error)

import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns

# MySQL connection details
config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Duke#7539',
    'database': 'stocks'
}

# Connect to MySQL
try:
    connection = mysql.connector.connect(**config)
    if connection.is_connected():
        cursor = connection.cursor()

        # Fetching data from the stock_data table
        select_query = "SELECT symbol, latest_price FROM stock_data"
        cursor.execute(select_query)
        data = cursor.fetchall()

        # Closing the database connection
        cursor.close()
        connection.close()

        if data:
            # Extracting symbols and latest prices
            symbols = [row[0] for row in data]
            prices = [row[1] for row in data]

            # Creating a bar plot using seaborn
            plt.figure(figsize=(12, 6))
            sns.set(style="whitegrid")
            plt.title("Latest Stock Prices")
            plt.xlabel("Symbols")
            plt.ylabel("Latest Price")
            sns.barplot(x=symbols, y=prices)
            plt.xticks(rotation=45)
            plt.tight_layout()

            # Show the plot
            plt.show()

        else:
            print("No data found in the stock_data table.")

    else:
        print("Connection failed!")

except mysql.connector.Error as error:
    print("Error while connecting to MySQL", error)


import mysql.connector
import seaborn as sns
import matplotlib.pyplot as plt

# MySQL connection details
config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Duke#7539',
    'database': 'stocks'
}

# Connect to MySQL
try:
    connection = mysql.connector.connect(**config)
    if connection.is_connected():
        cursor = connection.cursor()

        # Fetching data from the stock_data table
        select_query = "SELECT latest_price FROM stock_data"
        cursor.execute(select_query)
        data = cursor.fetchall()

        # Closing the database connection
        cursor.close()
        connection.close()

        if data:
            # Extracting latest prices
            prices = [row[0] for row in data]

            # Creating a distribution plot with a different color using seaborn
            plt.figure(figsize=(8, 6))
            sns.set(style="whitegrid")
            sns.histplot(prices, kde=True, bins=20, color='orange')  # Changing color to orange
            plt.title("Distribution of Latest Stock Prices")
            plt.xlabel("Latest Price")
            plt.ylabel("Frequency")
            plt.tight_layout()

            # Show the plot
            plt.show()

        else:
            print("No data found in the stock_data table.")

    else:
        print("Connection failed!")

except mysql.connector.Error as error:
    print("Error while connecting to MySQL", error)




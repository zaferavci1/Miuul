import pandas as pd

# CSV dosyasýnýn yolunu buraya ekleyin
csv_file_path = '/Users/zaferavci/downloads/txt.csv'
# Çýktý dosyasýnýn yolunu buraya ekleyin
output_file_path = '/Users/zaferavci/downloads/sql.txt'

# CSV dosyasýný okuyun
df = pd.read_csv('/Users/zaferavci/downloads/txt.csv', delimiter=';', decimal=',')

# CSV dosyasýndaki sütun adlarýný kontrol edin
print("Sütun Adlarý:", df.columns.tolist())

# SQL sorgularýný saklayacaðýmýz liste
queries = []

# Her bir satýr için SQL sorgusunu oluþturun
for _, row in df.iterrows():
    try:
        # NaN deðerleri kontrol edin ve NULL ile deðiþtirin
        id_value = int(row['Unnamed: 0']) if not pd.isna(row['Unnamed: 0']) else 'NULL'
        wallet = row['wallet'].replace("'", "''") if pd.notna(row['wallet']) else 'NULL'
        token_address = row['token_address'].replace("'", "''") if pd.notna(row['token_address']) else 'NULL'
        symbol = row['symbol'].replace("'", "''") if pd.notna(row['symbol']) else 'NULL'
        history_bought_cost = row['history_bought_cost'] if not pd.isna(row['history_bought_cost']) else 'NULL'
        usd_value = row['usd_value'] if not pd.isna(row['usd_value']) else 'NULL'
        realized_profit = row['realized_profit'] if not pd.isna(row['realized_profit']) else 'NULL'
        realized_pnl = row['realized_pnl'] if not pd.isna(row['realized_pnl']) else 'NULL'
        unrealized_profit = row['unrealized_profit'] if not pd.isna(row['unrealized_profit']) else 'NULL'
        unrealized_pnl = row['unrealized_pnl'] if not pd.isna(row['unrealized_pnl']) else 'NULL'
        total_profit = row['total_profit'] if not pd.isna(row['total_profit']) else 'NULL'
        total_profit_pnl = row['total_profit_pnl'] if not pd.isna(row['total_profit_pnl']) else 'NULL'
        avg_cost = row['avg_cost'] if not pd.isna(row['avg_cost']) else 'NULL'
        avg_sold = row['avg_sold'] if not pd.isna(row['avg_sold']) else 'NULL'
        buy_30d = row['buy_30d'] if not pd.isna(row['buy_30d']) else 'NULL'
        sell_30d = row['sell_30d'] if not pd.isna(row['sell_30d']) else 'NULL'
        sells = row['sells'] if not pd.isna(row['sells']) else 'NULL'
        price = row['price'] if not pd.isna(row['price']) else 'NULL'
        cost = row['cost'] if not pd.isna(row['cost']) else 'NULL'
        position_percent = row['position_percent'] if not pd.isna(row['position_percent']) else 'NULL'
        last_active_timestamp = int(row['last_active_timestamp']) if not pd.isna(row['last_active_timestamp']) else 'NULL'
        history_sold_income = row['history_sold_income'] if not pd.isna(row['history_sold_income']) else 'NULL'
        is_following = int(row['is_following'] == 'TRUE') if pd.notna(row['is_following']) else 0
        is_show_alert = int(row['is_show_alert'] == 'TRUE') if pd.notna(row['is_show_alert']) else 0
        
        query = f"""
INSERT INTO txt (ID, wallet, token_address, symbol, history_bought_cost, usd_value, realized_profit, realized_pnl, unrealized_profit, unrealized_pnl, total_profit, total_profit_pnl, avg_cost, avg_sold, buy_30d, sell_30d, sells, price, cost, position_percent, last_active_timestamp, history_sold_income, is_following, is_show_alert)
VALUES ({id_value}, '{wallet}', '{token_address}', '{symbol}', 
{history_bought_cost}, {usd_value}, {realized_profit}, {realized_pnl}, 
{unrealized_profit}, {unrealized_pnl}, {total_profit}, {total_profit_pnl}, 
{avg_cost}, {avg_sold}, {buy_30d}, {sell_30d}, {sells}, 
{price}, {cost}, {position_percent}, {last_active_timestamp}, 
{history_sold_income}, {is_following}, {is_show_alert});
"""
        queries.append(query)
    except KeyError as e:
        print(f"KeyError: {e} - Sütun adý bulunamadý!")
        
# SQL sorgularýný metin dosyasýna yazýn
with open(output_file_path, 'w') as file:
    file.write('\n'.join(queries))

print(f"SQL sorgularý '{output_file_path}' dosyasýna kaydedildi.")

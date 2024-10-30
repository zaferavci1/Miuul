import pandas as pd
import pyodbc

# CSV dosyasını yükleyin
df = pd.read_csv('/Users/zaferavci/downloads/txt.csv', delimiter=';', decimal=',')

# Bağlantı bilgilerinizi belirtin (burası genel bir örnektir)


# Bağlantı dizesi
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=txt;'  # Kullanmak istediğiniz veritabanı
    'UID=SA;'  # Kullanıcı adı
    'PWD=reallyStrongPwd123;'  # Şifreniz
    'Encrypt=yes;'  # Şifrelemeyi zorunlu kılmak için
    'TrustServerCertificate=yes;'  # Sunucu sertifikasına güvenmek için
)


# SQL komutlarını oluşturma
insert_statements = []

for index, row in df.iterrows():
    # Her satır için bir INSERT INTO sorgusu oluşturun
    sql = f"""
    INSERT INTO YourTableName (ID, wallet, token_address, symbol, history_bought_cost, usd_value, realized_profit, realized_pnl, unrealized_profit, unrealized_pnl, total_profit, total_profit_pnl, avg_cost, avg_sold, buy_30d, sell_30d, sells, price, cost, position_percent, last_active_timestamp, history_sold_income, is_following, is_show_alert)
    VALUES ({int(row['Unnamed: 0'])}, '{row['wallet']}', '{row['token_address']}', '{row['symbol']}', 
    {row['history_bought_cost']}, {row['usd_value']}, {row['realized_profit']}, {row['realized_pnl']}, 
    {row['unrealized_profit']}, {row['unrealized_pnl']}, {row['total_profit']}, {row['total_profit_pnl']}, 
    {row['avg_cost']}, {row['avg_sold']}, {row['buy_30d']}, {row['sell_30d']}, {row['sells']}, 
    {row['price']}, {row['cost']}, {row['position_percent']}, {int(row['last_active_timestamp'])}, 
    {row['history_sold_income']}, {int(row['is_following'] == 'TRUE')}, {int(row['is_show_alert'] == 'TRUE')});
    """
    insert_statements.append(sql)

# Tüm sorguları birleştirin ve SQL sunucusuna gönderin
cursor = conn.cursor()
for statement in insert_statements:  # Bu satır düzgün şekilde girintilendi
    cursor.execute(statement)
conn.commit()  # Bu satır da düzgün şekilde girintilendi

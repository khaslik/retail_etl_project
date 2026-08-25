import pandas as pd
import mysql.connector
outpuy_file = '../output/cleaned_retail.csv'
db_config = {
    'host':'localhost',
    'database':'retail_db',
    'user':'root',
    'password':'root'
}
def load_data():
    #Подключаем файл csv
    df = pd.read_csv(outpuy_file)
    print(f"Загружено: {len(df)}")
    #Подключаемся к БД
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    #Создаем таблицу
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        invoice VARCHAR(20),
        stock_code VARCHAR(20),
        description TEXT,
        quantity INT,
        invoice_date DATETIME,
        price DECIMAL(10,2),
        customer_id VARCHAR(20),
        country VARCHAR(50),
        year INT,
        month INT,
        day_of_week INT,
        hour INT,
        total_amount DECIMAL(10,2)
    )
    """)
    #Загружаем данные
    for _, row in df.iterrows():
        cursor.execute("""
        INSERT INTO sales (
            invoice, stock_code, description, quantity, invoice_date,
            price, customer_id, country, year, month, day_of_week, hour, total_amount
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            row['Invoice'],
            row['StockCode'],
            row['Description'][:255] if row['Description'] else None,
            row['Quantity'],
            row['InvoiceDate'],
            row['Price'],
            str(row['Customer ID']) if pd.notna(row['Customer ID']) else None,
            row['Country'],
            row['Year'],
            row['Month'],
            row['DayOfWeek'],
            row['Hour'],
            row['Total_Amount']
        ))

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    load_data()



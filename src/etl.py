import pandas as pd
import os
input_file = '../data/online_retail_II.csv' #Наименование файла csv
output_dir = '/output'
output_file = os.path.join(output_dir, 'cleaned_retail.csv')

def clean_data():
    # Создаём папку output
    os.makedirs(output_dir, exist_ok=True)

    # Читаем данные
    print("Загрузка данных...")
    df = pd.read_csv(input_file)

    print(f"Загружено записей: {len(df)}")
    print(f"Колонки: {df.columns.tolist()}")
    print(f"\nПропуски:\n{df.isnull().sum()}")
    print(f"\nТипы данных:\n{df.dtypes}")

    # Удаляем строки без Customer ID
    df = df.dropna(subset=['Customer ID'])
    print(f"После удаления пропусков Customer ID: {len(df)}")

    # Удаляем нулевые количества и цены
    df = df[df['Quantity'] != 0]
    df = df[df['Price'] > 0]
    print(f"После фильтрации Quantity и Price: {len(df)}")

    # Преобразуем дату
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

    # Создаём новые колонки
    df['Year'] = df['InvoiceDate'].dt.year
    df['Month'] = df['InvoiceDate'].dt.month
    df['DayOfWeek'] = df['InvoiceDate'].dt.dayofweek
    df['Hour'] = df['InvoiceDate'].dt.hour

    # Рассчитываем общую сумму
    df['Total_Amount'] = df['Quantity'] * df['Price']

    # Проверяем результат
    print(f"\nИтоговое количество записей: {len(df)}")
    print(f"Диапазон дат: {df['InvoiceDate'].min()} - {df['InvoiceDate'].max()}")

    # Сохраняем
    df.to_csv(output_file, index=False)
    print(f"Сохранено в {output_file}")

if __name__ == "__main__":
    clean_data()
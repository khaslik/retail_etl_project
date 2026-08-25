--Общая выручка по странам
SELECT country, SUM(total_amount) AS ИтоговаяСумма, COUNT(*) AS Кол_воТранзакций, COUNT(DISTINCT customer_id) AS УникальныеКлиенты
FROM sales
GROUP BY country
ORDER BY SUM(total_amount) DESC
--Топ 10 товаров по выручке
SELECT 
    stock_code AS КодТовара,
    description AS ОписаниеТовара,
    SUM(quantity) AS ИтоговоеКоличество,
    SUM(total_amount) AS ОбщийДоход
FROM sales
GROUP BY stock_code, description
ORDER BY SUM(total_amount) DESC
LIMIT 10;
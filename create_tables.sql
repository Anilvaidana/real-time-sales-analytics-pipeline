CREATE TABLE IF NOT EXISTS sales_clean (
    id INT PRIMARY KEY,
    product VARCHAR(50),
    amount NUMERIC(10,2),
    sale_date DATE,
    year_month VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS sales_agg_daily AS
SELECT sale_date,
       product,
       SUM(amount) AS revenue,
       COUNT(*) AS transactions
FROM sales_clean
GROUP BY sale_date, product;

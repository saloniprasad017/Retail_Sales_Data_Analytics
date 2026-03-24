-- Total Sales and Total Profit
SELECT 
    SUM(Sales) AS total_sales,
    SUM(Profit) AS total_profit
FROM cleaned_sales_data;


-- Sales by Region
SELECT 
    Region,
    SUM(Sales) AS total_sales,
    SUM(Profit) AS total_profit
FROM cleaned_sales_data
GROUP BY Region
ORDER BY total_sales DESC;


-- Sales by Category
SELECT 
    Category,
    SUM(Sales) AS total_sales,
    SUM(Profit) AS total_profit
FROM cleaned_sales_data
GROUP BY Category
ORDER BY total_sales DESC;


-- Top 10 Products by Sales
SELECT 
    Product_Name,
    SUM(Sales) AS revenue
FROM cleaned_sales_data
GROUP BY Product_Name
ORDER BY revenue DESC
LIMIT 10;


-- Customer Segment Analysis
SELECT 
    Segment,
    COUNT(DISTINCT Customer_ID) AS total_customers,
    SUM(Sales) AS total_sales,
    SUM(Profit) AS total_profit
FROM cleaned_sales_data
GROUP BY Segment;


-- Monthly Sales Trend
SELECT 
    DATE_FORMAT(Order_Date, '%Y-%m') AS month,
    SUM(Sales) AS monthly_sales
FROM cleaned_sales_data
GROUP BY month
ORDER BY month;


-- Profit by Sub Category
SELECT 
    Sub_Category,
    SUM(Profit) AS total_profit
FROM cleaned_sales_data
GROUP BY Sub_Category
ORDER BY total_profit DESC;

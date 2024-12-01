# Write your MySQL query statement below
SELECT 
    prices.product_id,
    IFNULL(ROUND(SUM(price* units) / SUM(units), 2), 0) average_price
FROM unitssold sold
RIGHT JOIN prices
    ON sold.product_id = prices.product_id 
    AND sold.purchase_date >= prices.start_date 
    AND sold.purchase_date <= prices.end_date
GROUP BY product_id
# Write your MySQL query statement below
SELECT
    product_name,
    year,
    price
FROM sales
LEFT JOIN product
    ON product.product_id = sales.product_id

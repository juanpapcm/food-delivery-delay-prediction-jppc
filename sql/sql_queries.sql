-- 1. Top 5 customer areas with highest average delivery time in the last 30 days
SELECT customer_area, AVG(delivery_time_min) AS avg_time
FROM deliveries
WHERE order_placed_at >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY customer_area
ORDER BY avg_time DESC
LIMIT 5;

-- 2. Average delivery time per traffic condition, by restaurant area and cuisine type
SELECT r.area AS restaurant_area, r.cuisine_type, d.traffic_condition, AVG(d.delivery_time_min) AS avg_delivery_time
FROM deliveries d
JOIN orders o ON d.delivery_id = o.delivery_id
JOIN restaurants r ON o.restaurant_id = r.restaurant_id
GROUP BY r.area, r.cuisine_type, d.traffic_condition;
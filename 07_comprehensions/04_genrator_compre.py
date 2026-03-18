daily_sales = [5, 10, 12, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

total_sales = sum(sale for sale in daily_sales if sale > 50)
print(total_sales)
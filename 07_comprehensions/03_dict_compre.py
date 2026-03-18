tea_price_inr = {
    "green": 20,
    "lemon": 30,
    "spiced": 25,
    "mint": 25  
}

tea_price_usd = {key: value * 0.8 for key, value in tea_price_inr.items()}
print(tea_price_usd)
users = [
    {"id": 1, "total": 100, "coupon": "p20"},
    {"id": 2, "total": 200, "coupon": "p30"},
    {"id": 3, "total": 300, "coupon": "p40"},
    {"id": 4, "total": 400, "coupon": "p50"},
    {"id": 5, "total": 500, "coupon": "p60"},
    {"id": 6, "total": 600, "coupon": "p70"},
    {"id": 7, "total": 700, "coupon": "p80"},
    {"id": 8, "total": 800, "coupon": "p90"},
    {"id": 9, "total": 900, "coupon": "p100"},
    {"id": 10, "total": 1000, "coupon": "p110"},
]

discounts = {
    "p20": (0.2, 0),
    "p30": (0.3, 0),
    "p90": (0,10),
}

for user in users:
   percent, fixed = discounts.get(user["coupon"], (0,0))
   discount = user["total"] * percent + fixed
   print(f"user id: {user['id']} total: {user['total']} discount: {discount}")
import asyncio
import time 

from concurrent.futures import ThreadPoolExecutor

def check_stock(item):
    print (f"Checking stock for {item}")
    time.sleep(2)
    return f"{item} is in stock: 54"

async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        stock_check = await loop.run_in_executor(pool, check_stock, "ginger chai")
        print(stock_check)


asyncio.run(main())
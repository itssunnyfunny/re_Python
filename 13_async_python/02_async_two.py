import asyncio

async def brew(name):
    print(f"brewing chai for {name}")
    await asyncio.sleep(2)
    
    print(f"chai brewed for {name}")


async def main():
    await asyncio.gather(brew("shani"), brew("priya"))

asyncio.run(main())
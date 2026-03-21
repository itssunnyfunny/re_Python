import asyncio

async def brew_chai():
    print("Brew chai")
    await asyncio.sleep(2)
    print("Chai brewed")

asyncio.run(brew_chai())
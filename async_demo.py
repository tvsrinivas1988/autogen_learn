import asyncio
import time
async def brew_coffee():
    print("Started Brewing Cofee")
    await asyncio.sleep(4)
    print("Coffee Brewing done")

async def toast_bagel():
    print("Started Toasting Bagel")
    await asyncio.sleep(3)
    print("Bagel Toasted")

async def main ():
    start = time.time()

    coffee = brew_coffee()
    bagel = toast_bagel()

    results = await asyncio.gather(coffee,bagel)

    end = time.time()

    print(f"Time : {end - start:.2f} minutes")
asyncio.run(main())
import asyncio



async def work(name):
    print(f"working {name}")
    await asyncio.sleep(2)
    print(f"done {name}")


async def main():

    t1 = asyncio.create_task(work("ABCD"))
    t2 = asyncio.create_task(work("ZDFGH"))

    await t1
    await t2



asyncio.run(main())




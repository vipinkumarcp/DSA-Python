
import asyncio




async def work(name):

    print(f"started work {name}")
    await asyncio.sleep(2)
    print(f"work completed {name}")


async def main():

    await asyncio.gather(work("A"),work("B"))



asyncio.run(main())
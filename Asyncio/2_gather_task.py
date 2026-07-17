
import asyncio


async def work(name):

    print(f"started {name}")

    await asyncio.sleep(2)

    print(f"ended {name}")


async def looping():

    for i in range(5):
        print(i)


async def main():
    await asyncio.gather(work("A"),looping())


asyncio.run(main())
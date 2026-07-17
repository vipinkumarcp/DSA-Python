import time
import asyncio

def time_measure(name):

    print(f"start {name}")

    time.sleep(2)

    print(f"stop time {name}")


async def main():

    t1 = asyncio.create_task(asyncio.to_thread(time_measure,"A"))
    t2 = asyncio.create_task(asyncio.to_thread(time_measure,"B"))

    await t1
    await t2





if __name__ == '__main__':
    
    asyncio.run(main())



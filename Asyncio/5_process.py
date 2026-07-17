import asyncio
import time
from concurrent.futures import ProcessPoolExecutor


def time_measure(name):
    print(f"start {name}")
    time.sleep(2)
    print(f"stop {name}")
    return f"{name} completed"


async def main():

    loop = asyncio.get_running_loop()

    with ProcessPoolExecutor() as executor:

        t1 = loop.run_in_executor(executor, time_measure, "A")
        t2 = loop.run_in_executor(executor, time_measure, "B")

        result1 = await t1
        result2 = await t2

        print(result1)
        print(result2)


if __name__ == "__main__":
    asyncio.run(main())
import asyncio
from urllib.parse import urlparse
import aiohttp

urls = [ "https://www.python.org", "https://www.github.com", "https://www.google.com" ]


async def fecth(url,session):

    urlInfo = urlparse(url)

    print(f"hostname {urlInfo.hostname}")
    print(f"host {urlInfo.netloc}")

    async with session.get(url) as response:

        text = await response.text()

        print(f"resposne : {response.status}")


async def main():

    async with aiohttp.ClientSession() as session:

        task = [fecth(url,session) for url in urls]

        await asyncio.gather(*task)


asyncio.run(main())
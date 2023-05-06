import asyncio
import time


async def seconds_counter():
    count = 0
    while True:
        print("second passed")
        count += 1
        await asyncio.sleep(1)


async def manager():
    lock = asyncio.Lock()

    asyncio.create_task(seconds_counter())



if __name__ == '__main__':
    loop = asyncio.run(manager())

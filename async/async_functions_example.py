import asyncio
import time


async def count_from(n, name="none", speed=0.5):
    while n > 0:
        print(f"counted {n} from {name}")
        await asyncio.sleep(speed)
        n -= 1


async def seconds_counter():
    while True:
        print("second passed")
        await asyncio.sleep(1)


async def captcha():
    while True:
        input("Вы всё ещё тут?")
        await asyncio.sleep(60)


async def manager():
    asyncio.create_task(captcha())
    task1 = asyncio.create_task(count_from(10, name="first counter"))
    task2 = asyncio.create_task(count_from(15, name="second counter", speed=0.1))
    asyncio.create_task(seconds_counter())
    await task2
    print("task 2 finished")
    await task1
    print("task 1 finished")


if __name__ == '__main__':
    loop = asyncio.run(manager())

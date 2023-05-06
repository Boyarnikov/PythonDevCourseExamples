import asyncio
import time


class Wallet:
    money = 100
    lock = None


async def pay(value, w: Wallet):
    m = w.money
    print(f"Запрошено {value}, на счету {m}")
    if m < value:
        print(f"Отказано")
        return False
    print(f"В процессе")

    if w.lock.locked():
        print("Кошелёк занят, ожидаю")

    with w.lock:
        print("Кошелёк захвачен, в процессе")
        m = w.money
        await asyncio.sleep(1)
        print(f"Снятие")
        w.money = m - value


async def manager():

    w = Wallet()
    w.lock = asyncio.Lock()

    payment1 = asyncio.create_task(pay(10, w))
    payment2 = asyncio.create_task(pay(10, w))
    await payment1
    await payment2
    print(f"{w.money} на счету")


if __name__ == '__main__':
    loop = asyncio.run(manager())

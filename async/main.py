import asyncio
import time
import os
import aiohttp

from typing import Iterable, Optional, Tuple, Generator

URL = "https://docs.python.org/3.8/archives"
CHUNK = 1024


async def download_from_web(file, s):
    url = URL + "/" + file
    async with s.get(url) as response:
        if response.status == 404:
            raise RuntimeError("File not found")
        writer = write_file(file)
        next(writer)
        while True:
            chunk = await response.content.read(CHUNK)
            try:
                writer.send(chunk)
            except StopIteration:
                break


def write_file(file) -> Generator[None, Optional[bytes], None]:
    if not os.path.exists("files/"):
        os.mkdir("files/")
    with open(os.path.join("files/", file), "wb") as f:
        while True:
            chunk = yield
            if not chunk:
                break
            else:
                f.write(chunk)


async def download_file(file, s):
    try:
        await download_from_web(file, s)
    except RuntimeError:
        print(f"Runtime Error downloading the {file}")
        return False
    print(f"downloaded {file}")
    return True


async def download_files(files):
    async with aiohttp.ClientSession() as s:
        res = await asyncio.gather(*[download_file(file, s) for file in files])
    return sum([1 if r else 0 for r in res])


def main():
    start_time = time.time()
    to_download = list([
        f"python-3.8.{i}-docs-html.zip" for i in range(13)
    ])

    downloaded = 0
    for i in to_download:
        downloaded += asyncio.run(download_files([i]))

    result_time = time.time() - start_time
    return downloaded, result_time


def main_async():
    start_time = time.time()
    to_download = list([
        f"python-3.8.{i}-docs-html.zip" for i in range(13)
    ])

    downloaded = asyncio.run(download_files(to_download))

    result_time = time.time() - start_time
    return downloaded, result_time


if __name__ == '__main__':
    downloaded_amount, time = main_async()
    print(f"done, downloaded {downloaded_amount} files in {time} seconds")

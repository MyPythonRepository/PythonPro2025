import asyncio
import aiohttp
from pathlib import Path


async def download_image(session, url, filename):
    print(f"Start downloading {filename}")
    async with session.get(url) as resp:
        content = await resp.read()
        Path("images").mkdir(exist_ok=True)
        with open(f"images/{filename}", "wb") as f:
            f.write(content)
    print(f"Finished downloading {filename}")


async def download_many(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for idx, url in enumerate(urls):
            task = asyncio.create_task(download_image(session, url, f"img_{idx}.jpg"))
            tasks.append(task)
        await asyncio.gather(*tasks)


async def report_status():
    print("Status: Download started")
    print("Status: Waiting for downloads to finish...")


async def set_result_later(future, delay_task):
    await delay_task
    future.set_result("All images downloaded")
    print("set_result_later: future result has been set")


async def wait_for_completion_with_future(future):
    result = await future
    print(f"wait_for_completion_with_future: Received result: {result}")


async def notify_completion():
    print("Download finished. Sending notification...")


async def main():
    image_urls = [
        "https://picsum.photos/200/300",
        "https://picsum.photos/300/200",
        "https://picsum.photos/250/250",
        "https://picsum.photos/310/310",
        "https://picsum.photos/220/330",
    ]

    future = asyncio.Future()

    download_task = asyncio.create_task(download_many(image_urls))

    awaitables = [
        report_status(),
        notify_completion(),
        wait_for_completion_with_future(future),
        set_result_later(future, download_task)
    ]

    await asyncio.gather(download_task, *awaitables)


if __name__ == "__main__":
    asyncio.run(main())

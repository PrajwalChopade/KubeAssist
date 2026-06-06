# crawler/crawler.py

import asyncio
from pathlib import Path
from urllib.parse import urlparse

from crawl4ai import AsyncWebCrawler
from bs4 import BeautifulSoup

RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)

URLS = [
    "https://kubernetes.io/docs/concepts/workloads/controllers/deployment/",
    "https://kubernetes.io/docs/concepts/workloads/pods/",
    "https://kubernetes.io/docs/concepts/services-networking/service/",
    "https://kubernetes.io/docs/concepts/storage/persistent-volumes/",
    "https://kubernetes.io/docs/concepts/configuration/configmap/",
    "https://kubernetes.io/docs/concepts/security/",
]


def clean_filename(url: str):
    path = urlparse(url).path.strip("/")
    return path.replace("/", "_")


async def crawl_page(crawler, url):
    result = await crawler.arun(url=url)

    if not result.success:
        print(f"Failed: {url}")
        return

    html = result.html

    soup = BeautifulSoup(html, "html.parser")

    # Remove noise
    for tag in soup.find_all(
        ["nav", "header", "footer", "aside"]
    ):
        tag.decompose()

    main = soup.find("main")

    if not main:
        print(f"No main content: {url}")
        return

    text = main.get_text("\n", strip=True)

    filename = clean_filename(url)

    with open(
        RAW_DIR / f"{filename}.txt",
        "w",
        encoding="utf-8",
    ) as f:
        f.write(text)

    print(f"Saved {filename}")


async def main():
    async with AsyncWebCrawler() as crawler:

        for url in URLS:
            await crawl_page(crawler, url)


if __name__ == "__main__":
    asyncio.run(main())
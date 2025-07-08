import asyncio
import sys
from config import JAVADOC_URL 
from crawl4ai import AsyncWebCrawler
from utils.scraper_utils import fetch_and_process_custom_table
from utils.data_utils import save_venues_to_csv
import os

async def crawl_java_docs(url):
    
    class_name = os.path.basename(url).replace(".html", "")

    filename = f"dataset/{class_name}_methods.csv"

    async with AsyncWebCrawler(
        headless=True,
        disable_images=True,
        javascript=True,
        timeout=30
    ) as crawler:
        print(f"Scraping content from {url}...")
        table_data, no_results = await fetch_and_process_custom_table(crawler, url)

        if no_results:
            print("No data found.")
        else:
            save_venues_to_csv(table_data, filename)
            print(f"Saved {len(table_data)} entries to '{filename}'")

            

async def main():
    url = sys.argv[1] if len(sys.argv) > 1 else JAVADOC_URL
    await crawl_java_docs(url)


if __name__ == "__main__":
    asyncio.run(main())

import asyncio
from crawl4ai import AsyncWebCrawler
from utils.scraper_utils import fetch_and_process_custom_table
from utils.data_utils import save_venues_to_csv

async def crawl_java_docs(url):
    async with AsyncWebCrawler(
        headless=True,
        disable_images=True,
        javascript=True,
        timeout=30
    ) as crawler:
        print(f"Scraping content from {url}...")
        table_data, no_results = await fetch_and_process_custom_table(crawler, url)

        if no_results:
            print("⚠️ No data found.")
        else:
            save_venues_to_csv(table_data, "dataset/StringBuffer_methods.csv")
            print(f"✅ Saved {len(table_data)} entries to 'StringBuffer_methods.csv'")

async def main():
    url = "https://docs.oracle.com/javase/8/docs/api/java/lang/StringBuffer.html"
    await crawl_java_docs(url)

if __name__ == "__main__":
    asyncio.run(main())

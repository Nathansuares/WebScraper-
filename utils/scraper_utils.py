from bs4 import BeautifulSoup

async def fetch_and_process_custom_table(crawler, url):
    result = await crawler.arun(url)  # ✅ Final fix
    soup = BeautifulSoup(result.html, "html.parser")

    rows = soup.select(".blockList .memberSummary tbody tr")
    print(f"Found {len(rows)} method rows")

    table_data = []
    for row in rows:
        try:
            modifier = row.select_one(".colFirst").get_text(strip=True)
            method = row.select_one(".colSecond").get_text(strip=True)
            description = row.select_one(".colLast .block").get_text(strip=True)

            table_data.append({
                "modifier_and_type": modifier,
                "method": method,
                "description": description
            })
        except Exception as e:
            print("❌ Error processing row:", e)
            continue

    return table_data, len(table_data) == 0

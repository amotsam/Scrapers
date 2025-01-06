import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import utils

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Configuration
BASE_URL = "https://www.tapuz.co.il/forums"  # Forum base URL
OUTPUT_FILE = "data/rawData/forums.csv"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

# Initialize session with retry logic
session = requests.Session()
retry = Retry(total=5, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

def parse_forums_data(html):
    """Parse the HTML content and extract required forum data."""
    try:
        soup = BeautifulSoup(html, 'html.parser')
        data = []
        # Extract forum rows from the HTML
        forums = soup.find_all('div', class_='forum-list-item')  # Update class as per website structure
        for forum in forums:
            title = forum.find('a', class_='forum-title').text.strip()
            link = forum.find('a', class_='forum-title')['href']
            topics = forum.find('span', class_='topics-count').text.strip()
            messages = forum.find('span', class_='messages-count').text.strip()
            data.append({
                "Title": title,
                "Link": link,
                "Topics": topics,
                "Messages": messages
            })
        return data
    except Exception as e:
        logging.error(f"Failed to parse data: {e}")
        return []


def main():
    """Main function to run the forum scraper."""
    logging.info("Forum scraping started...")
    html = fetch_html(BASE_URL)
    if html:
        data = parse_forums_data(html)
        if data:
            utils.save_to_csv(data, OUTPUT_FILE)
    logging.info("Forum scraping completed.")

if __name__ == "__main__":
    main()

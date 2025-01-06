import pandas as pd
import logging
from requests.adapters import HTTPAdapter
import requests
from urllib3 import Retry
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


def save_to_csv(data, file_path):
    """Save the extracted data to a CSV file."""
    try:
        df = pd.DataFrame(data)
        df.to_csv(file_path, index=False, encoding='utf-8')
        logging.info(f"Data saved successfully to {file_path}")
    except Exception as e:
        logging.error(f"Failed to save data to {file_path}: {e}")


def Init_session():
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retries)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session

def fetch_html(url,session):
    """Fetch the HTML content of a URL."""

    try:
        response = session.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch {url}: {e}")
        return None



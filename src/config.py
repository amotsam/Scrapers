# Configuration for scrapers
SCRAPER_CONFIGS = {
    "ALL_DOMAINS": ["forums", "jobs", "news", "reviews", "shopping"],
    "forums": {
        "BASE_URL": "https://www.tapuz.co.il/forums/",
        "RAW_OUTPUT_FILE": "../data/rawData/forums.csv",
        "CLEANED_OUTPUT_FILE": "../data/cleaned/cleaned_forums_data.csv",
        "TRANSFORMED_OUTPUT_FILE": "../data/transformed/transformed_forums_data.csv",
        "HEADERS": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
    },
    "jobs": {
        "BASE_URL": "https://www.drushim.co.il/%D7%9E%D7%A9%D7%A8%D7%95%D7%AA-%D7%9C%D7%9C%D7%90-%D7%A7%D7%95%D7%A8%D7%95%D7%AA-%D7%97%D7%99%D7%99%D7%9D/?cv=1",
        "RAW_OUTPUT_FILE": "../data/rawData/jobs.csv",
        "CLEANED_OUTPUT_FILE": "../data/cleaned/cleaned_jobs_data.csv",
        "TRANSFORMED_OUTPUT_FILE": "../data/transformed/transformed_jobs_data.csv",
        "HEADERS": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
    },
    "news": {
        "BASE_URL": "https://www.ynet.co.il/",
        "RAW_OUTPUT_FILE": "../data/rawData/news.csv",
        "CLEANED_OUTPUT_FILE": "../data/cleaned/cleaned_news_data.csv",
        "TRANSFORMED_OUTPUT_FILE": "../data/transformed/transformed_news_data.csv",
        "HEADERS": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
    },
    "reviews": {
        "BASE_URL": "https://www.seret.co.il/critics/moviecriticszone.asp",
        "RAW_OUTPUT_FILE": "../data/rawData/reviews.csv",
        "CLEANED_OUTPUT_FILE": "../data/cleaned/cleaned_reviews_data.csv",
        "TRANSFORMED_OUTPUT_FILE": "../data/transformed/transformed_reviews_data.csv",
        "HEADERS": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
    },
    "shopping": {
        "BASE_URL": "https://lcp.co.il/",
        "RAW_OUTPUT_FILE": "../data/rawData/shopping.csv",
        "CLEANED_OUTPUT_FILE": "../data/cleaned/cleaned_shopping_data.csv",
        "TRANSFORMED_OUTPUT_FILE": "../data/transformed/transformed_shopping_data.csv",
        "HEADERS": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
    }
}

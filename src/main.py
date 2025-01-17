import logging
import utils
from config import SCRAPER_CONFIGS
from importlib import import_module


def loginng():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )


def validate_data(file_path, validation_rules):
    """Validate data against defined rules."""
    import pandas as pd
    try:
        data = pd.read_csv(file_path)
        # Check required columns
        for col in validation_rules.get("required_columns", []):
            if col not in data.columns:
                logging.error(f"Validation failed: Missing column '{col}' in {file_path}")
                return False
        # Check non-empty columns
        for col in validation_rules.get("non_empty_columns", []):
            if data[col].isnull().any():
                logging.error(f"Validation failed: Column '{col}' contains empty values in {file_path}")
                return False
        logging.info(f"Validation passed for {file_path}")
        return True
    except Exception as e:
        logging.error(f"Error during validation for {file_path}: {e}")
        return False


def run_scraper(domain):
    logging.info(f"Starting pipeline for {domain}...")
    try:
        config = SCRAPER_CONFIGS[domain]
        session = utils.Init_session()

        # Dynamically import scraper module
        scraper_module = import_module(f"scripts.scrapers.{domain}Scraper")

        # Scrape raw data
        html_scraped = scraper_module.fetch_html(config["BASE_URL"], session)
        if not html_scraped:
            raise RuntimeError(f"Scraping failed for {domain}")

        if hasattr(scraper_module, "parse_data"):
            raw_data = scraper_module.parse_data(html_scraped)
            utils.save_to_csv(raw_data, config["RAW_OUTPUT_FILE"])

            # Validate scraped data
            if not validate_data(config["RAW_OUTPUT_FILE"], config["validation"]["scraped"]):
                raise ValueError(f"Validation failed for scraped data in {domain}")

        else:
            raise AttributeError(f"'parse_data' function not found in {domain}Scraper")

        # Clean data
        cleaner_module = import_module(f"scripts.cleanning.{domain}Preproccess")
        cleaned_data = cleaner_module.clean(config["RAW_OUTPUT_FILE"])
        utils.save_to_csv(cleaned_data, config["CLEANED_OUTPUT_FILE"])

        # Transform data
        transformer_module = import_module(f"scripts.transformation.{domain}_feature_eng")
        transformed_data = transformer_module.transform(config["CLEANED_OUTPUT_FILE"])
        utils.save_to_csv(transformed_data, config["TRANSFORMED_OUTPUT_FILE"])

        # Validate transformed data
        if not validate_data(config["TRANSFORMED_OUTPUT_FILE"], config["validation"]["transformed"]):
            raise ValueError(f"Validation failed for transformed data in {domain}")

        logging.info(f"Pipeline for {domain} completed successfully.")
    except Exception as e:
        logging.error(f"Error in pipeline for {domain}: {e}")


def main():
    loginng()
    logging.info("Starting scraping project...")

    for domain in SCRAPER_CONFIGS["ALL_DOMAINS"]:
        try:
            run_scraper(domain)
        except Exception as e:
            logging.error(f"Failed to process domain {domain}: {e}")

    logging.info("All scraping tasks completed.")
if __name__ == "__main__":
    main()

# stock_market_data_scraper
Purpose: Solely responsible for scraping data from various sources (NSE/BSE, news websites, company reports)

This repository is responsible for scraping stock market data from various sources for the Stock Market Simulator project.

## Structure

- `config/`: Configuration files.
- `data_acquisition/`: Contains subpackages for data acquisition:
    - `scrapers/`:  Scraper scripts for different sources (NSE/BSE, news, etc.).
    - `data_cleaning/`: Scripts for cleaning scraped data.
    - `data_analysis/`: Scripts for basic data analysis (initial checks).
- `utils/`: Utility functions.
- `data/raw_data/`:  Directory to store raw scraped data.

## Setup

1. Clone this repository: `git clone <repository_url>`
2. Navigate to the repository directory: `cd stock_market_data_scraper`
3. Install dependencies: `pip install -r requirements.txt`
4. Install the package: `pip install -e .`  (This installs it in "editable" mode, useful during development)

## Usage

(Will be updated as scrapers are implemented)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
# open_souq_scraper
# Python Web Scraper for Car Listings

This project is a Python script that scrapes car listing data from a website and stores the data in a CSV file.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have Python installed on your machine. You can download Python [here](https://www.python.org/downloads/).

This project also requires the following Python libraries:
- requests
- json
- BeautifulSoup
- pandas
- datetime
- os

You can install these packages using pip:

```bash
pip install requests beautifulsoup4 pandas

Usage
To use this script, you need to specify the base URL of the car listings page and the total number of pages you want to scrape.
base_url = "https://om.opensooq.com/en/cars/cars-for-sale/bmw/bmw-m3?search=true"
total_pages = 5
cars_details = scrape_cars(base_url, total_pages)


# Methodology

## Data Source

The data was collected from the **Books to Scrape** website, a public website designed for practicing web scraping.

Website:
https://books.toscrape.com/

## Data Collection

Python was used to automate the extraction of book information from the website.

The scraper navigated through all 50 pages of the website and collected data for 1000 books.

The following information was extracted:

- Book Title
- Price (£)
- Rating

## Data Cleaning

After scraping, the dataset was cleaned using Pandas.

The following cleaning steps were performed:

- Removed the "£" symbol from the Price column.
- Converted the Price column to numeric (float).
- Converted book ratings from text to numeric values (1–5).
- Verified that no duplicate records were introduced during scraping.

## Data Storage

The cleaned dataset was exported as:

- books_all_pages.csv

The dataset was then imported into Microsoft Excel for Exploratory Data Analysis (EDA).

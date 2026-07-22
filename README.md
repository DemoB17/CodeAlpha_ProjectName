# 📚 CodeAlpha Web Scraping Project

## Project Overview

This project was completed as part of the CodeAlpha Data Analytics Internship.

The objective was to scrape book information from the **Books to Scrape** website using Python. The collected data was cleaned, exported to CSV, analyzed using Microsoft Excel, and visualized to uncover meaningful insights.

## Skills Demonstrated

- Web Scraping
- Data Collection
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Data Visualization
- Microsoft Excel
- Power BI
- Python Programming
- Git Version Control
- GitHub Documentation

---

## Objectives

- Scrape book information from a website using Python.
- Extract book titles, prices, and ratings.
- Clean and prepare the dataset.
- Export the data to CSV format.
- Perform Exploratory Data Analysis (EDA).
- Create visualizations to identify trends and patterns.

---

## Tools & Technologies

- Python
- Requests
- BeautifulSoup
- Pandas
- Microsoft Excel 2019
- Git
- GitHub

---

## Dataset Information

**Source:** Books to Scrape

Website:
https://books.toscrape.com/

**Records Collected:** 1000 Books

**Features:**
- Title
- Price (£)
- Rating (1–5)

---

## Repository Structure

```text
CodeAlpha-Web-Scraping-Books/
│
├── README.md
├── requirements.txt
├── data/
├── documentation/
├── screenshots/
├── src/
└── visualizations/
```

---

## Project Workflow

1. Scraped all 50 pages of the Books to Scrape website.
2. Extracted book titles, prices, and ratings.
3. Cleaned the Price column.
4. Converted ratings from text to numeric values.
5. Exported the cleaned dataset to CSV.
6. Performed exploratory data analysis in Excel.
7. Created visualizations to communicate insights.

---

## Key Results

- Successfully scraped **1000 books**.
- Cleaned and transformed the dataset for analysis.
- Produced summary statistics and visualizations.
- Built a reusable dataset for further analysis.

  
## How to Run

1. Clone the repository.

```bash
git clone <repository-url>
```

2. Install dependencies.

```bash
pip install -r requirements.txt
```

3. Navigate to the `src` folder.

4. Run:

```bash
python books_scraper.py
```
---

## Future Improvements

- Scrape additional book attributes such as availability and category.
- Automate scheduled data collection.
- Store scraped data in a SQL database.
- Build an interactive Power BI dashboard with filters.
- Deploy the scraper as an automated workflow.

---

## Author

**Ademola Alaanu**

CodeAlpha Data Analytics Intern

import requests
from bs4 import BeautifulSoup
import pandas as pd


books = []

for page in range(1, 51):

   
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"

  
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    book_list = soup.find_all("article", class_="product_pod")
    print(f"Page {page}: Found {len(book_list)} books")
    
    for book in book_list:

        
        title = book.find("h3").find("a")["title"]
        price = book.find("p", class_="price_color").get_text(strip=True)
        rating = book.find("p", class_="star-rating")["class"][1]
    
        books.append({
            "Title": title,
            "Price": price,
            "Rating": rating
        })

df = pd.DataFrame(books)
df["Price"] = (
    df["Price"]
    .str.replace("Â£", "", regex=False)
    .str.replace("£", "", regex=False)
    .astype(float)
)
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}
average_price = df["Price"].mean()

print(f"Average Price: £{average_price:.2f}")
df["Rating"] = df["Rating"].map(rating_map)
print(df.head(10))
print("\nData Information:")
print(df.info())
df.to_csv("books_all_pages.csv", index=False)

print(f"\nTotal books scraped: {len(df)}")
print("Data saved successfully as books_all_pages.csv")
# Import required libraries

# Create an empty list to store book data

# Loop through all 50 pages

# Extract title, price, and rating

# Convert the list to a DataFrame

# Clean the Price column

# Convert Rating to numeric

# Save the data to a CSV file
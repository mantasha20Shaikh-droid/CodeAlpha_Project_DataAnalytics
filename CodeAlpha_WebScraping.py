# Data Analytics Task

# INSTALL REQUIRED LIBRARIES
!pip install beautifulsoup4 requests pandas matplotlib seaborn textblob wordcloud -q

# TASK 1 : WEB SCRAPING
'''
TASK 1: Web Scraping
- Extract data using BeautifulSoup
- Navigate HTML structure
- Collect custom dataset
- Save dataset for analysis
- Dynamic and unique scraping project
'''

print("TASK 1 : WEB SCRAPING")
# Import Libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# Website for Practice
url = "http://quotes.toscrape.com"

# Send Request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Empty Lists
quotes_data = []

# Extract Multiple Information
quotes = soup.find_all("div", class_="quote")

for q in quotes:

    text = q.find("span", class_="text").text
    author = q.find("small", class_="author").text

    # Extract Tags
    tags = [tag.text for tag in q.find_all("a", class_="tag")]

    quotes_data.append({
        "Quote": text,
        "Author": author,
        "Tags": ", ".join(tags),
        "Length": len(text),
        "Scraped_Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

# Create DataFrame
quotes_df = pd.DataFrame(quotes_data)

# Save Dataset
quotes_df.to_csv("dynamic_quotes_dataset.csv", index=False)

# Display Output
print("\n Custom Dataset Created Successfully")
print("\nTop 5 Scraped Records:\n")
print(quotes_df.head())
print("\nDataset Shape :", quotes_df.shape)
print("\nCSV File Saved as -> dynamic_quotes_dataset.csv")

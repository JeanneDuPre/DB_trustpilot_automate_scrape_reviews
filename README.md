# DB_trustpilot_automate_scrape_reviews
[![Scrape DB reviews all trustpilot](https://github.com/JeanneDuPre/DB_trustpilot_automate_scrape_reviews/actions/workflows/scrape_all_reviews.yml/badge.svg)](https://github.com/JeanneDuPre/DB_trustpilot_automate_scrape_reviews/actions/workflows/scrape_all_reviews.yml)
<br>
There is a Python script that scrapes data from Trustpilot for Deutsche Bahn reviews and stores it in a MongoDB database. 

# <strong>Scrape_3_pages.py</strong> does the following:

   1. Imports necessary libraries and modules:
    - requests for making HTTP requests.
    - pandas for data manipulation and storage.
    - datetime for working with date and time.
    - os for handling file paths and directories.
    - pymongo for interacting with a MongoDB database.
     
  2. Defines a function fetch_articles(page) that fetches review articles from a specific page on Trustpilot's website and returns them as a list of BeautifulSoup objects.

  3. Defines a function extract_article_data(articles) that extracts data from each review article, such as author, location, date, text, rating, etc., and returns a list of dictionaries containing this data.

  4. Defines a function save_to_csv(df, csv_filename) that saves the extracted data to a CSV file.

  5. In the main() function:<br>
    - Specifies the start and end page numbers for scraping (currently set to 1 to 3).<br>
    - Fetches articles from the start page.<br>
    - Extracts article data from the fetched articles.<br>
    - Converts the extracted data into a Pandas DataFrame.<br>
    - Generates a CSV filename based on the current date and time and saves the DataFrame to a CSV file.<br>
    - Establishes a connection to a MongoDB database using a connection string.<br>
    - Converts the DataFrame to a list of dictionaries for MongoDB insertion.<br>
    - Specifies the MongoDB database and collection names based on the current date and time.<br>
    - Inserts the data into the MongoDB collection.<br>

Finally, it runs the main() function when the script is executed.<br>

# <strong>GitHub Workflow</strong>: 

# <strong>Streamlit App</strong>:

TODO Trustpilot, MongoDB, GitHub Actions, data 

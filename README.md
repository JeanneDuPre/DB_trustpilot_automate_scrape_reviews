DB_trustpilot_automate_scrape_reviews

There is a Python script that scrapes data from Trustpilot for Deutsche Bahn reviews and stores it in a MongoDB database. 

This script does the following:

  1. Imports necessary libraries and modules:
    - requests for making HTTP requests.
    - pandas for data manipulation and storage.
    - datetime for working with date and time.
    - os for handling file paths and directories.
    - pymongo for interacting with a MongoDB database.
     
  2. Defines a function fetch_articles(page) that fetches review articles from a specific page on Trustpilot's website and returns them as a list of BeautifulSoup objects.

  3. Defines a function extract_article_data(articles) that extracts data from each review article, such as author, location, date, text, rating, etc., and returns a list of dictionaries containing this data.

  4. Defines a function save_to_csv(df, csv_filename) that saves the extracted data to a CSV file.

  5. In the main() function:
    - Specifies the start and end page numbers for scraping (currently set to 1 to 3).
    - Fetches articles from the start page.
    - Extracts article data from the fetched articles.
    - Converts the extracted data into a Pandas DataFrame.
    - Generates a CSV filename based on the current date and time and saves the DataFrame to a CSV file.
    - Establishes a connection to a MongoDB database using a connection string.
    - Converts the DataFrame to a list of dictionaries for MongoDB insertion.
    - Specifies the MongoDB database and collection names based on the current date and time.
    - Inserts the data into the MongoDB collection.

Finally, it runs the main() function when the script is executed.

# TODO Trustpilot, MongoDB, GitHub Actions, data 

from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime
import os


def fetch_articles(page): 
    URL= f"https://de.trustpilot.com/review/www.db.de?page={page}"
    response = requests.get(URL,headers= {"Accept-Language": "de-DE"})
    soup = BeautifulSoup(response.content, features='lxml')
    articles = soup.find_all('article', class_= "paper_paper__1PY90 paper_outline__lwsUX card_card__lQWDv card_noPadding__D8PcU styles_reviewCard__hcAvl")
    return articles

def extract_articles_data(item): 
    author_element = item.find('span', class_= "typography_heading-xxs__QKBS8 typography_appearance-default__AAY17")
    author = author_element.text if author_element else None
        
    land_element = item.find('div', class_= "typography_body-m__xgxZ_ typography_appearance-subtle__8_H2l styles_detailsIcon__Fo_ua")
    land = land_element.text if land_element else None
        
    date_element = item. find('p', class_= "typography_body-m__xgxZ_ typography_appearance-default__AAY17")
    date = date_element.text if date_element else None
        
    text_element = item.find('p', class_= "typography_body-l__KUYFJ typography_appearance-default__AAY17 typography_color-black__5LYEn")
    text = text_element.text if text_element else None
        
    nützlich_element = item.find('span', class_= "typography_body-m__xgxZ_ typography_appearance-inherit__D7XqR styles_usefulLabel__qz3JV")
    nützlich = nützlich_element.text if nützlich_element else None
        
    title_element = item.find('h2', class_= "typography_heading-s__f7029 typography_appearance-default__AAY17")
    title = title_element.text if title_element else None
        
    bewertung_element = item.find('span', class_= "typography_body-m__xgxZ_ typography_appearance-subtle__8_H2l")
    bewertung = bewertung_element.text if bewertung_element else None

    sterne_element = item.find('div', class_="star-rating_starRating__4rrcf star-rating_medium__iN6Ty")
    img_tag = sterne_element.find('img')  # Find the img tag within the 'sterne_element'
    sterne_alt = img_tag.get('alt') if img_tag else None  # Extract the 'alt' attribute value

        
    date_online_element = item.find('time', class_= "data-service-review-date-time-ago")
    date_online = date_online_element.text if date_online_element else None
        
    article = {
        'date': date,
        'title': title,
        'text': text,
        'bewertung': bewertung,
        'sterne': sterne_alt,
        'author': author,
        'land': land,
        'nützlich': nützlich,
        'date_online': date_online
    }
    return article

def save_to_csv(df):
    data_folder = "data"
    os.makedirs(data_folder, exist_ok=True)
    current_datetime = datetime.now().strftime("%Y-%m-%d")
    csv_filename = f'DB_all_review_Stand_{current_datetime}.csv'
    csv_filepath = os.path.join(data_folder, csv_filename)
    df.to_csv(csv_filepath, index=False)

def main():
    start_page = 1
    articles_list = []

    while True:
        articles = fetch_articles(start_page)
        
        if not articles:
            break
        
        for item in articles:
            data = extract_articles_data(item)
            articles_list.append(data)
        
        start_page += 1

    df = pd.DataFrame(articles_list)
    save_to_csv(df)

if __name__ == "__main__":
    main()

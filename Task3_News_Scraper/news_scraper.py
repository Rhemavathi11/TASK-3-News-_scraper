import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"
OUTPUT_FILE = "headlines.txt"


def fetch_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text


def extract_headlines(html):
    soup = BeautifulSoup(html, "html.parser")

    headlines = []

    for tag in soup.find_all(["h1", "h2", "h3"]):
        text = tag.get_text(strip=True)

        if text and text not in headlines:
            headlines.append(text)

    return headlines


def save_headlines(headlines):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        for i, headline in enumerate(headlines, start=1):
            file.write(f"{i}. {headline}\n")


def main():
    try:
        html = fetch_html(URL)
        headlines = extract_headlines(html)
        save_headlines(headlines)

        print("News headlines scraped successfully!")
        print(f"Total headlines saved: {len(headlines)}")
        print(f"Saved in: {OUTPUT_FILE}")

    except requests.exceptions.RequestException as error:
        print("Error while fetching website:", error)


main()
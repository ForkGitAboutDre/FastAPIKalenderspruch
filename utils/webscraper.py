from bs4 import BeautifulSoup
import re
import requests


def clean(item: str):
    return len(item) > 15 and "-" not in item and "\n*" not in item and "Übersetzung" not in item


def remove_brackets(item: str):
    if "[" in item or "]" in item or "/" in item:
        return item.translate({ord(c): None for c in "[]/"})
    else:
        return item


def get_quotes():
    url = "https://de.wikiquote.org/w/index.php?title=Deutsche_Sprichw%C3%B6rter&action=edit"
    page = requests.get(url)

    regex_quotes = re.compile(r'"([^"]*)"')

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="wpTextbox1")
    dirty_quotes = re.findall(regex_quotes, results.prettify())
    cleaned_quotes = list(filter(clean, dirty_quotes))
    formatted_quotes = list(map(remove_brackets, cleaned_quotes))

    return dict(zip(range(0, len(formatted_quotes)), formatted_quotes))

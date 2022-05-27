from typing import Union

from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from bs4 import BeautifulSoup
import requests
app = FastAPI()
url = "https://de.wikiquote.org/w/index.php?title=Deutsche_Sprichw%C3%B6rter&action=edit"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id = "wpTextbox1")
print(results.prettify())
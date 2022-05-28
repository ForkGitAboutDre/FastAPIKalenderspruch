import datetime
from typing import Union

from fastapi import FastAPI
from utils import webscraper, quotepicker

description = """
Kalenderspruch API helps you do awesome stuff.


You will be able to:

* **get calendar saying for today** 
* **get calendar saying for specified days**
"""
tags_metadata = [{
    "name": "Quotes",
    "description": "the date must be the following format \"2018-01-01\""
}]
app = FastAPI(title="Kalenderspruch",
              description=description,
              version="1.0.0",
              contact={
                  "name": "my github account",
                  "url": "http://github.com/forkgitaboutdre"
              },
              tags_metadata=tags_metadata)


quotes = webscraper.get_quotes()


@app.get("/quote/")
def read_quote(date: Union[datetime.date, None] = None):
    if date is None:
        return quotepicker.get_quote_of_today(quotes)
    else:
        return quotepicker.get_quote_of_day(quotes, date)

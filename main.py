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

app = FastAPI(title="Kalenderspruch",
              description=description,
              version="1.0.0",
              contact={
                  "name": "my github account",
                  "url": "https://github.com/ForkGitAboutDre/FastAPIKalenderspruch"
              }
              )


quotes = webscraper.get_quotes()


@app.get("/quote/")
def read_quote(date: Union[datetime.date, None] = None):
    if date is None:
        return quotepicker.get_quote_of_day(quotes, datetime.date.today())
    else:
        return quotepicker.get_quote_of_day(quotes, date)

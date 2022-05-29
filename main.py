import datetime
from typing import Union

from fastapi import FastAPI, Query
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
                  "url": "https://github.com/ForkGitAboutDre"
              }
              )


quotes = webscraper.get_quotes()


@app.get("/quote/")
def read_quote(date: Union[datetime.date, None] = Query(default=None, examples={
            "normal": {
                "summary": "A date",
                "description": "A date with format YYYY-MM-DD works correctly.",
                "value": "2022-05-29"
            },
            "micros after epoch": {
                "summary": "An example with an integer",
                "description": "it automatically gets converted to a date based on milliseconds after epoch",
                "value": 1123123121323
            },
            "None":{
                "summary": "no date set.",
                "description": "get the quote of today"
    }
        },
    )
):
    if date is None:
        return quotepicker.get_quote_of_day(quotes, datetime.date.today())
    else:
        return quotepicker.get_quote_of_day(quotes, date)

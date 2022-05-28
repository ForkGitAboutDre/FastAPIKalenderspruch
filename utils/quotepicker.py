from datetime import datetime
from delorean import Delorean
from datetime import date
import random


def get_quote_of_today(quotes:dict):
    rand_index = __generate_random_number(date.today(), len(quotes))
    return quotes[rand_index]


def get_quote_of_day(quotes: dict, lookup_date: date):
    rand_index = __generate_random_number(lookup_date, len(quotes))
    return quotes[rand_index]


def __generate_random_number(lookup_date: date, max_generated_number: int):
    time = datetime(year=lookup_date.year, month=lookup_date.month, day=lookup_date.day)
    time_with_timezone = Delorean(time, timezone='GMT')
    micros_after_epoch = time_with_timezone.start_of_day.timestamp()
    random.seed(micros_after_epoch)
    return random.randrange(0, max_generated_number)




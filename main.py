import sqlite3
from sqlite3 import Error
import requests
from bs4 import BeautifulSoup
import pprint
import queries
from scraping import scrapetelex
import timing
from apscheduler.schedulers.blocking import BlockingScheduler

_PATH_ = "/Users/cx-ray/PycharmProjects/IntermediateProjects/WebScrape/db/pythonsqlite.db"

if __name__ == '__main__':
    with queries.create_connection(_PATH_):
        queries.create_telex_table(_PATH_)

scheduler = BlockingScheduler()
scheduler.add_job(scrapetelex, 'interval', seconds=10)
scheduler.start()

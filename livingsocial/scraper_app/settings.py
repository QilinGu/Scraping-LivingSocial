#!/usr/bin/env python
# coding=utf-8

BOT_NAME = 'livingsocial'

SPIDER_MODULES =['scraper_app.spiders']

ITEM_PIPELINES = {'scraper_app.pipelines.LivingSocialPipeline': 300}

DATABASE = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': 'Summer',
    'password': 'mima161616',
    'database': 'scrape'
}

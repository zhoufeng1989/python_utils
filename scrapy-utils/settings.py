# Scrapy settings for scrapy-utils project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
# change scrapy-utils to your crawl project name
BOT_NAME = 'scrapy-utils'

DOWNLOAD_DELAY = 2.5
SPIDER_MODULES = ['scrapy-utils.spiders']
NEWSPIDER_MODULE = 'scrapy-utils.spiders'

ITEM_PIPELINES = [
    'scrapy-utils.pipelines.DownloadImagesPipeline']

DOWNLOADER_MIDDLEWARES = {
    'scrapy-utils.extendedmiddleware.CheckUrlMiddleware': 50,
    'scrapy-utils.extendedmiddleware.ProxyMiddleware': 300,
    'scrapy-utils.extendedmiddleware.UserAgentMiddleware': 400,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None}

USER_AGENT_LIST = [
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/28.0.1468.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.11 '
    '(KHTML, like Gecko) Chrome/23.0.1271.6 Safari/537.11',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.11 '
    '(KHTML, like Gecko) Chrome/23.0.1271.17 Safari/537.11',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 '
    '(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) '
    'Chrome/19.0.1084.9 Safari/536.5',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) '
    'Chrome/19.0.1061.0 Safari/536.3',
    'Mozilla/5.0 (X11; CrOS i686 1193.158.0) AppleWebKit/535.7 '
    '(KHTML, like Gecko) Chrome/16.0.912.75 Safari/535.7',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) '
    'Chrome/15.0.872.0 Safari/535.2',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 '
    '(KHTML, like Gecko) Chrome/14.0.811.0 Safari/535.1',
    'Mozilla/6.0 (Windows; U; Windows NT 7.0; en-US; rv:1.9.0.8) '
    'Gecko/2009032609 Firefox/3.0.9 (.NET CLR 3.5.30729)',
    'Mozilla/5.0 (X11; U; Linux x86_64; en-GB; rv:1.9.0.9) Gecko/2009042113 '
    'Ubuntu/8.10 (intrepid) Firefox/3.0.9',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.9) Gecko/2009042113 '
    'Linux Mint/6 (Felicia) Firefox/3.0.9',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.0.4) Firefox/3.0.8)',
    'Mozilla/5.0 (X11; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 '
    'Firefox/3.0.7',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0']

MYSQL_CONFIG = {
    'db': 'db_name',
    'user': 'username',
    'pw': 'password',
    'charset': 'utf8',
    'host': '127.0.0.1',
    'port': 3306}

REDIS_CONFIG = {
    'host': '127.0.0.1',
    'port': 6379,
    'url_prefix': 'scrapy-utils:url:'
}

LOG_FILE = 'scrapy-utils.log'
LOG_STDOUT = True
COOKIES_ENABLED = False

PROXIES_LIST = [
    # your proxies list here
    # 'ip:port'
]

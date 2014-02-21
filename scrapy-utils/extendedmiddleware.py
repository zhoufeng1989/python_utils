from settings import USER_AGENT_LIST, REDIS_CONFIG, PROXIES_LIST
from scrapy.exceptions import IgnoreRequest
from scrapy import log
import random
import redis
redis_client = redis.StrictRedis(
    host=REDIS_CONFIG['host'], port=REDIS_CONFIG['port']
)


class UserAgentMiddleware(object):
    '''This middleware allow spiders to rotate user_agents'''
    def process_request(self, request, spider):
        ua = random.choice(USER_AGENT_LIST)
        if ua:
            request.headers['User-Agent'] = ua


class ProxyMiddleware(object):
    '''use proxy when crawl'''
    def process_request(self, request, spider):
        proxy = random.choice(PROXIES_LIST)
        if proxy:
            log.msg('proxy is %s url is %s' % (proxy, request.url))
            request.meta['proxy'] = 'http://' + proxy


class CheckUrlMiddleware(object):
    '''This middleware allow spiders to avoid repeated request an url'''
    def process_request(self, request, spider):
        url = request.url
        if redis_client.get(REDIS_CONFIG['url_prefix'] + url):
            log.msg('request is dumplicated:%s' % url)
            raise IgnoreRequest

    def process_response(self, request, response, spider):
        if request.url in spider.start_urls:
            pass
        elif redis_client.get(REDIS_CONFIG['url_prefix'] + request.url):
            log.msg('request is dumpocated in response:%s' % request.url)
        else:
            if redis_client.set(REDIS_CONFIG['url_prefix'] + request.url, 1):
                log.msg('request is remember:%s' % request.url)
        return response

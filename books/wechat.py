#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

from base import BaseFeedBook
from lib.urlopener import URLOpener
import urllib

__author__ = 'VictorHong'

# 使用https://www.freefullrss.com/ 该网站转化为全文
API_URL = 'https://www.freefullrss.com/feed.php?url=%s&max=5&links=preserve&exc=1&submit=Create+Full+Text+RSS'

def getBook():
    return WeChatReader

class WeChatReader(BaseFeedBook):
    title                 = u'Victor的微信订阅'
    description           = u'这是Victor的微信精选订阅，将在Kindle上阅读！'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_xueqiu.gif"
    coverfile             = "cv_xueqiu.jpg"
    max_articles_per_feed = 5
    oldest_article        = 1
    network_timeout       = 60

    feeds = [
            (u'每日学英语', API_URL % urllib.quote('https://rsshub.app/wechat/ershicimi/10589'), True),
            (u'进击的Coder', API_URL % urllib.quote('https://rsshub.app/wechat/ershicimi/117'), True),
            (u'玩转VS Code', API_URL % urllib.quote('https://rsshub.app/wechat/ershicimi/8956'), True),
            (u'Quora文选', API_URL % urllib.quote('https://rsshub.app/wechat/ershicimi/10863'), True),
            (u'Python数据科学', API_URL % urllib.quote('https://rsshub.app/wechat/ershicimi/3250'), True),
            (u'GitHubDaily', API_URL % urllib.quote('https://rsshub.app/wechat/ershicimi/6679'), True),
            (u'码农翻身', API_URL % urllib.quote('https://rsshub.app/wechat/ershicimi/57'), True),
            (u'CVer', API_URL % urllib.quote('https://rsshub.app/wechat/ershicimi/2698'), True),
            (u'雅思哥', API_URL % urllib.quote('https://rsshub.app/wechat/ershicimi/10411'), True),
            (u'程序员小灰', API_URL % urllib.quote('https://rsshub.app/wechat/ershicimi/155'), True),
            (u'199IT互联网数据中心', API_URL % urllib.quote('https://rsshub.app/wechat/ershicimi/6387'), True),
            (u'非著名程序员', API_URL % urllib.quote('https://rsshub.app/wechat/ershicimi/172'), True),
    ]
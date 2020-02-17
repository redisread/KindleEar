#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

from base import BaseFeedBook
import re, urllib
from lib.urlopener import URLOpener
from bs4 import BeautifulSoup
import json
from config import SHARE_FUCK_GFW_SRV

__author__ = 'victorhong'

def getBook():
    return MyWechat

class MyWechat(BaseFeedBook):
    title                 = u'微信公众号'
    description           = u'微信订阅内容。。。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_xueqiu.gif"
    coverfile             = "cv_xueqiu.jpg"
    oldest_article        = 3   #距离几天的文章
    #fulltext_by_readability = False # 取消自动处理网页

    feeds = [ (u'英语', 'https://rsshub.app/wechat/ershicimi/10589'),
              (u'今日话题', 'https://rsshub.app/wechat/ce//5d059616f1531303a827d8a9'),]
    
    def url4forwarder(self, url):
        #生成经过转发器的URL
        return SHARE_FUCK_GFW_SRV % urllib.quote(url)
    
    def fetcharticle(self, url, opener, decoder):
        #链接网页获取一篇文章
        return BaseFeedBook.fetcharticle(self, self.url4forwarder(url), opener, decoder)